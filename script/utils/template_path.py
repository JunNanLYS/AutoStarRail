"""模板图目录"""

import os
import config

IMAGE_ROOT_PATH = os.path.join(config.abspath, "images\\")  # 图片根目录
CALYX_GOLD_PATH = IMAGE_ROOT_PATH + "calyx_gold\\"  # 拟造花萼的目录
CALYX_RED_PATH = IMAGE_ROOT_PATH + "calyx_red\\"  # 拟造花萼(赤)目录
SHADOW_PATH = IMAGE_ROOT_PATH + "shadow\\"  # 凝滞虚影的目录
CAVERN_PATH = IMAGE_ROOT_PATH + "cavern\\"  # 侵蚀隧道的目录
ECHO_OF_WAR_PATH = IMAGE_ROOT_PATH + "echo\\"  # 历战回响的目录
COMMISSION_PATH = IMAGE_ROOT_PATH + "commission\\"  # 委托任务的目录
CHARACTER_PATH = IMAGE_ROOT_PATH + "character\\"  # 角色的目录
WORLD_PATH = IMAGE_ROOT_PATH + "world\\"  # 世界的目录

# 杂 more
PHONE = IMAGE_ROOT_PATH + r"phone.png"  # 手机
MANDATE = IMAGE_ROOT_PATH + r"mandate.png"  # 任务书
BOOK = IMAGE_ROOT_PATH + r"book.png"  # 星际和平书
BOOK2 = IMAGE_ROOT_PATH + r"book2.png"  # 星际和平书界面
INDEX = IMAGE_ROOT_PATH + r"index.png"  # 生存索引
INDEX_SELECTED = IMAGE_ROOT_PATH + r"indexSelected.png"  # 选中状态下的"生存索引"
DAILY_TASK = IMAGE_ROOT_PATH + r"dailyTask.png"  # 每日任务
DAILY_TASK_SELECTED = IMAGE_ROOT_PATH + r"dailyTaskSelected.png"  # 选中状态下的"每日任务"
NO_STAMINA = IMAGE_ROOT_PATH + r"noStamina.png"  # 没有体力
CANCEL = IMAGE_ROOT_PATH + r"cancel.png"  # 取消按钮
CONFIRM = IMAGE_ROOT_PATH + r"confirm.png"  # 确认按钮
SELECTED_CONFIRM = IMAGE_ROOT_PATH + r"selectedConfirm.png"  # 被选中的确认按钮
FUEL = IMAGE_ROOT_PATH + r"fuel.png"  # 燃料
SELECTED_FUEL = IMAGE_ROOT_PATH + r"selectedFuel.png"  # 被选中的燃料
STELLAR_JADE = IMAGE_ROOT_PATH + r"stellarJade.png"  # 星穹
SELECTED_STELLAR_JADE = IMAGE_ROOT_PATH + r"selectedStellarJade.png"  # 被选中的星穹
AUTO_FIGHT = IMAGE_ROOT_PATH + r"autoFight.png"  # 自动战斗(未开启)
AUTO_FIGHT_2 = IMAGE_ROOT_PATH + r"autoFight2.png"  # 自动战斗(开启)
AUTO_FIGHT_3 = IMAGE_ROOT_PATH + r"autoFight3.png"  # 自动战斗(开启)
AUTO_FIGHT_4 = IMAGE_ROOT_PATH + r"autoFight4.png"  # 自动战斗(开启)
AREA_NAVIGATION = IMAGE_ROOT_PATH + r"areaNavigation.png"  # 区域导航
BALL_NAVIGATION = IMAGE_ROOT_PATH + r"ballNavigation.png"  # 星球导航

# 拟造花萼 calyx
CALYX_GOLD_1 = CALYX_GOLD_PATH + "1.png"
CALYX_GOLD_2 = CALYX_GOLD_PATH + r"2.png"
CALYX_GOLD_3 = CALYX_GOLD_PATH + r"3.png"
CALYX_RED_1 = CALYX_RED_PATH + r"1.png"
CALYX_RED_2 = CALYX_RED_PATH + r"2.png"
CALYX_RED_3 = CALYX_RED_PATH + r"3.png"
CALYX_RED_4 = CALYX_RED_PATH + r"4.png"
CALYX_RED_5 = CALYX_RED_PATH + r'5.png'
CALYX_RED_6 = CALYX_RED_PATH + r"6.png"
CALYX_RED_7 = CALYX_RED_PATH + r"7.png"

# 凝滞虚影 Stagnant shadow
SHADOW_1 = SHADOW_PATH + r"1.png"  # 空海之形
SHADOW_2 = SHADOW_PATH + r"2.png"  # 巽风之形
SHADOW_3 = SHADOW_PATH + r"3.png"  # 鸣雷之形
SHADOW_4 = SHADOW_PATH + r"4.png"  # 炎华之形
SHADOW_5 = SHADOW_PATH + r"5.png"  # 锋芒之形
SHADOW_6 = SHADOW_PATH + r"6.png"  # 霜晶之形
SHADOW_7 = SHADOW_PATH + r"7.png"  # 幻光之形
SHADOW_8 = SHADOW_PATH + r"8.png"  # 冰凌之形
SHADOW_9 = SHADOW_PATH + r"9.png"  # 震厄之形
SHADOW_10 = SHADOW_PATH + r"10.png"  # 天人之形
SHADOW_11 = SHADOW_PATH + r"11.png"
SHADOW_12 = SHADOW_PATH + r"12.png"

# 侵蚀隧道 cavern
CAVERN_1 = CAVERN_PATH + r"1.png"
CAVERN_2 = CAVERN_PATH + r"2.png"
CAVERN_3 = CAVERN_PATH + r"3.png"
CAVERN_4 = CAVERN_PATH + r"4.png"
CAVERN_5 = CAVERN_PATH + r"5.png"
CAVERN_6 = CAVERN_PATH + r"6.png"
CAVERN_7 = CAVERN_PATH + r"7.png"

# 历战余响 Echo Of War
ECHO_1 = ECHO_OF_WAR_PATH + r"1.png"  # 毁灭回响
ECHO_2 = ECHO_OF_WAR_PATH + r"2.png"  # 存护回响
ECHO_3 = ECHO_OF_WAR_PATH + r"3.png"  # 丰饶回响

# 副本 Copies
CHALLENGE = IMAGE_ROOT_PATH + r"challenge.png"  # 副本的挑战按钮
CHALLENGE_COMPLETED = IMAGE_ROOT_PATH + r"challengeCompleted.png"  # 挑战成功
START_CHALLENGE = IMAGE_ROOT_PATH + r"startChallenge.png"  # 开始挑战按钮
ADD_CHALLENGE = IMAGE_ROOT_PATH + r"addChallenge.png"  # 添加挑战副本的次数按钮
TRANSMISSION = IMAGE_ROOT_PATH + r"transmission.png"  # 传送按钮

# 委托
COMMISSION = COMMISSION_PATH + r"commission.png"  # 委托按钮
COMMISSION_PENDING = COMMISSION_PATH + r"commissionPending.png"  # 右上角有感叹号的委托按钮
IS_COMMISSION = COMMISSION_PATH + r"isCommission.png"  # 委托界面
PENDING = COMMISSION_PATH + r"pending.png"  # 待领取
RECEIVE_COMMISSIONING_REWARD = COMMISSION_PATH + r"receiveCommissioningReward.png"  # 领取委托的奖励按钮
RE_COMMISSION = COMMISSION_PATH + r"re-commission.png"  # 重新委托按钮

START_GAME = IMAGE_ROOT_PATH + r"startGame.png"  # 启动器的开始游戏
ENTER_GAME = IMAGE_ROOT_PATH + r"enterGame.png"  # 进入游戏
EXIT_COPIES = IMAGE_ROOT_PATH + r"exitCopies.png"  # 退出挑战

# 角色
ARROW = CHARACTER_PATH + r"arrow.png"  # 向上箭头
ARROW_DOWN = CHARACTER_PATH + r"arrowDown.png"  # 向下箭头
ARROW_LEFT = CHARACTER_PATH + r"arrowLeft.png"  # 向左箭头
ARROW_RIGHT = CHARACTER_PATH + r"arrowRight.png"  # 后右箭头
LOCAL_ARROW = CHARACTER_PATH + r"localArrow.png"  # 本地箭够

# 世界
QUESTION_MASK = WORLD_PATH + r"questionMask.png"  # 问号
WARNING = WORLD_PATH + r"warning.png"  # 感叹号
SELECT_MONSTER = WORLD_PATH + r"selectMonster.png"  # 选中敌人
SELECT_JAR = WORLD_PATH + r"selectJar.png"  # 选中罐子
