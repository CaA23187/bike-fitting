# 输入参考值
# 跨高79, 臂长60, 胸高124, 身高173
def main():
    print("-----------------------------------------------------")
    print("云Fitting计算器, 计算方式来自微博@摸发虱痒, 结果仅供参考。")
    print("         使用前需测量跨高、臂长、胸高、身高             ")
    print("---------------!!!所有长度单位均为cm------------------\n\n")
    dangao = float(input("请输入跨高(cm): "))
    C_switch = int(input("请输入stack校正值, 竞技需求与能力 0; 普通 1; 舒适取向 2 :   "))
    if C_switch == 0:
        C = -2
    if C_switch == 1:
        C = 0
    if C_switch == 2:
        C = 3
    else:
        C = 0
    STR_switch = int(input("请输入STR值, 竞技需求与能力 0; 普通 1; 舒适取向 2 :   "))
    if STR_switch == 0:
        STR = 1.36
    if STR_switch == 1:
        STR = 1.48
    if STR_switch == 2:
        STR = 1.6
    else:
        STR = 1.48
    zuogao = 0.885 * dangao
    stack = (0.69*dangao) + C
    reach = stack/STR
    Label = (0.66*dangao) + 2
    print('---------车架结果(此数值对于东亚人群似乎偏小)----------')
    print(f'|坐垫高(cm): {zuogao:.2f}\t|stack(cm): {stack:.2f}\t|reach(cm): {reach:.2f}\t|车架标号(cm): {Label:.2f}')
    print('----------------------------------------------------')

    bichang = float(input("请输入臂长(cm):   "))
    xionggao = float(input("请输入胸高(cm):   "))
    quganchang = xionggao - dangao

    high = float(input("请输入身高(cm):   "))
    if high<150 or high>200:
        print("身高范围低于150cm或高于200cm, 无法计算")
        return 0
    
    posture_switch = int(input("请输入姿势参数, 直立 0, 中立 1, 进取 2:   "))
    if posture_switch == 0:
        posture_param = 0.52
    if posture_switch == 1:
        posture_param = 0.535
    if posture_switch == 2:
        posture_param = 0.545
    else:
        posture_param = 0.535


    luocha_param_table = [
        ["0-2", "2-3", "3-7"],
        ["1-3", "3-5", "5-8"],
        ["2-4", "4-7", "7-12"],
        ["3-5", "5-9", "9-14"],
        ["4-6", "6-10", "10-16"]
    ]

    high_switch = int(high//10-15)
    print("请选择希望的落差, 建议范围为: ", luocha_param_table[high_switch][posture_switch], "(cm)")
    luocha_param = float(input("请输入落差(cm):   ")) - 2 # 原博主说这一步减去20mm会让结果相对更为合理

    stack_plus = (zuogao*0.96) - luocha_param
    reach_plus = (quganchang + bichang)*posture_param - zuogao*0.29 + 10
    print('---------手部位置计算结果----------')
    print(f'|stack+(cm): {stack_plus:.2f}\t|reach+(cm): {reach_plus:.2f}')
    print('----------------------------------------------------')

if __name__ == "__main__":
    main()    
