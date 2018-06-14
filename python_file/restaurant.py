class Restaurant():
      """一次模拟餐厅的状态的尝试"""

      def __init__(this,restaurant_name,cuisine_type):
            """初始化属性restaurant_name,cuisine_type"""
            this.restaurant_name = restaurant_name
            this.cuisine_type = cuisine_type


      def describe_restaurant(this):
            """返回属性的相关消息"""
            print(this.restaurant_name+' ' +this.cuisine_type)

      def open_restaurant(this):
            """提示餐馆正在营业"""
            print(this.restaurant_name.title()+' '+'is running now,welcome to hear!!!')
#第一个实例            
restaurant = Restaurant('mingzui','shaguoju')
restaurant.describe_restaurant()
restaurant.open_restaurant()


#第二个实例
muslim_restaurant = Restaurant('河州','拉面馆')
muslim_restaurant.describe_restaurant()
muslim_restaurant.open_restaurant()

#第三个实例

new_restaurant = Restaurant('穆一家','拉面馆')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
