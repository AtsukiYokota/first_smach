# ROS smach練習用リポジトリ
## インストール
```
cd <catkin_ws>/src
git clone https://github.com/AtsukiYokota/first_smach.git
cd <catkin_ws>
catkin_make
source devel/setup.bash
rospack profile
```
## 使い方
### 状態機械の組み上げと観測
```
rosrun smach_viewer smach_viewer.py # 状態観測
rosrun first_smach test_create_statemachine.py # 状態組み上げ
rosrun first_smach dummy_pub3.py # 外部からの指示(入れ替え可)
```

