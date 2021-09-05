import pandas as pd

ITEM_MASTER_CSV_PATH="./item_master.csv"
RECEIPT_FOLDER="./receipt"

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self):
    # 課題2
        item_code = input("商品コードを入力して下さい：")
        self.item_order_list.append(item_code)
        
    # 課題1
    def view_item_list(self):
        for order_item_code in self.item_order_list:
            for m in self.item_master:
                if order_item_code == m.item_code:
                    print("{}".format(m.item_name)+"の金額: "+"{}".format(m.price))

def add_item_master_by_csv(csv_path):
        print("------- マスタ登録開始 ---------")
        item_master=[]
        count=0
        try:
            item_master_df=pd.read_csv(csv_path,dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
            for item_code,item_name,price in zip(list(item_master_df["item_code"]),list(item_master_df["item_name"]),list(item_master_df["price"])):
                item_master.append(Item(item_code,item_name,price))
                print("{}({})".format(item_name,item_code))
                count+=1
            print("{}品の登録を完了しました。".format(count))
            print("------- マスタ登録完了 ---------")
            return item_master
        except:
            print("マスタ登録が失敗しました")
            print("------- マスタ登録完了 ---------")
            sys.exit()
            
### メイン処理
def main():
    # マスタ登録
    item_master=add_item_master_by_csv(ITEM_MASTER_CSV_PATH) # CSVからマスタへ登録
    order=Order(item_master) 
    # item_master=[]
    # path = "./item_master.csv"
    # df = pd.read_csv(path)
    # item_master.append(Item(df["item_code"], df["item_name"], df["price"]))

    # オーダー登録
    order=Order(item_master)
    order.add_item_order()
    
    # オーダー表示
    order.view_item_list()
 

if __name__ == "__main__":
    main()