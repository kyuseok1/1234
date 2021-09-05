# 출처 : https://young0823.tistory.com/301

import pyupbit
import schedule
import time

access = "1Yjmb4vnCUwxUAe3YSGv1M9tdW8fwna4kavNfFkl"
secret = "STPXspK2V5hz4rVRCimwdbwlemg4HgIb6gGGF2Id"
upbit = pyupbit.Upbit(access, secret)


    # 투자금 : 5,5000,000원
    # 현  금 :   500,000원
    # 총자금 : 5,000,000원
    # 기본비율 : BTC:XRP:ADA:ETH 비율은 50%:15%:15%:15%:5%. 즉 0.5 : 0.15 : 0.15 : 0.15 : 0.05
    # 운용범위 : 각 0.5% 즉, 0.05 증감 가능
                # BTC는 0.495 ~  [0.5]  ~ 0.505  -->   2,375,000 ~ [2,500,000] ~ 2,625,000 (+125,000)
                # XRP는 0.145 ~  [0.15] ~ 0.155  -->     725,000 ~  [750,000]  ~ 775,000
                # ADA는 0.145 ~  [0.15] ~ 0.155  -->     725,000 ~  [750,000]  ~ 775,000
                # ETH는 0.145 ~  [0.15] ~ 0.155  -->     725,000 ~  [750,000]  ~ 775,000
                # DOGE는 0.045 ~ [0.05] ~ 0.055  -->     225,000 ~  [250,000]  ~ 275,000

print()
print(" AutoTrading Start - for the Financial Independence......!!!")


def job(): # 아래 들여쓰기된 코드를 주기적으로 실행

    print(" 각 코인별로 보유하고 있는 비율을 분석합니다......" )


    a = upbit.get_balance("KRW") -500000

    b = upbit.get_balance("KRW-BTC") * pyupbit.get_current_price("KRW-BTC")
    c = upbit.get_balance("KRW-XRP") * pyupbit.get_current_price("KRW-XRP")
    d = upbit.get_balance("KRW-ADA") * pyupbit.get_current_price("KRW-ADA")
    f = upbit.get_balance("KRW-ETH") * pyupbit.get_current_price("KRW-ETH")
    h = upbit.get_balance("KRW-DOGE") * pyupbit.get_current_price("KRW-DOGE")

    e = a + b + c+ d + f + h


    print("------------------------------------------------------------------------------------------")
    print(" ---> BTC 보유액 :", f"{float(b):.1f}", "   XRP 보유액 : ", f"{float(c):.1f}", "   XEP 비율 :", f"{float(c/e):.3f}", "(적정 : 0.15)")
    time.sleep(1)    


    if c/e <= 0.145 :                                     # 총자금(e)에서 XRP가 0.145 이하가 되면.....,
        upbit.buy_market_order("KRW-XRP", 0.15*e-c)       # XRP를 사고

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고 
            
        if b/e >= 0.505 :                                 # BTC가 0.505 이상일땐
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  # BTC를 팔고


    if c/e >= 0.155 :                                     # 총자금(e)에서 XRP가 0.155 이상이 되면.....,
        upbit.sell_market_order("KRW-XRP", (c-0.15*e) / pyupbit.get_current_price("KRW-XRP"))     # XRP를 팔고

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고
            
        if b/e >= 0.505 :                                 # BTC가 0.505 이상일땐  
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  # BTC를 팔고


    time.sleep(1)    
    print(" ---> BTC 보유액 :", f"{float(b):.1f}", "   ADA 보유액 : ", f"{float(d):.1f}", "   ADA 비율 :", f"{float(d/e):.3f}", "(적정 : 0.15)")
    time.sleep(1)    


    if d/e <= 0.145 :                                     # 총자금(e)에서 ADA가 0.145 이하가 되면.....,
        upbit.buy_market_order("KRW-ADA", 0.15*e-d)       # ADA를 사고                      

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고
            
        if b/e >= 0.505 :                                 # BTC가 0.505 이상일땐  
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  # BTC를 팔고


    if d/e >= 0.155 :                                     # 총자금(e)에서 XRP가 0.155 이상이 되면.....,
        upbit.sell_market_order("KRW-ADA", (d-0.15*e) / pyupbit.get_current_price("KRW-ADA"))     # ADA를 팔고

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고
            
        if b/e >= 0.505 :                                 # BTC가 0.505 이상일땐    
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  # BTC를 팔고


    print(" ---> BTC 보유액 :", f"{float(b):.1f}", "   ETH 보유액 : ", f"{float(f):.1f}", "   ETH 비율 :", f"{float(f/e):.3f}", "(적정 : 0.15)")
    time.sleep(1)    


    if f/e <= 0.145 :                                     # 총자금(e)에서 ETH가 0.145 이하가 되면.....,
        upbit.buy_market_order("KRW-ETH", 0.15*e-f)       # ETH를 사고

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고
            
        if b/e >= 0.505 :                                 # BTC가 0.505 이상일땐
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  # BTC를 팔고


    if f/e >= 0.155 :                                     # 총자금(e)에서 ETH가 0.155 이상이 되면.....,
        upbit.sell_market_order("KRW-ETH", (f-0.15*e) / pyupbit.get_current_price("KRW-ETH"))     # ETH를 팔고

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고
            
        if b/e >= 0.505 :                                 # BTC가 0.505 이상일땐
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  # BTC를 팔고


    print(" ---> BTC 보유액 :", f"{float(b):.1f}", "  DOGE 보유액 : ", f"{float(h):.1f}", "  DOGE 비율 :", f"{float(h/e):.3f}", "(적정 : 0.05)")
    print( )
    time.sleep(1)    


    if h/e <= 0.045 :                                     # 총자금(e)에서 DOGE가 0.045 이하가 되면.....,
        upbit.buy_market_order("KRW-DOGE", 0.05*e-h)      # DOGE를 사고

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고
            
        if b/e >= 0.505 :                                 # BTCE가 0.505 이상일땐 
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  # BTC를 팔고


    if h/e >= 0.055 :                                     # 총자금(e)에서 DOGE가 0.055 이상이 되면.....,
        upbit.sell_market_order("KRW-DOGE", (h-0.05*e) / pyupbit.get_current_price("KRW-DOGE"))   # DOGE를 팔고

        if b/e <= 0.495 :                                 # BTC가 0.495 이하일땐
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    # BTC를 사고
            
        if b/e >= 0.505 :                                 # BTC가 0.505 이상일땐   
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))    # BTC를 팔고


schedule.every().minute.at(":00").do(job)
# schedule.every().minute.at(":15").do(job)
# schedule.every(1).hour.do(job)  # 1시간마다 한번씩 실행
# schedule.every().hour.do(job)   # 1시간마다 한번씩 실행

while True:
    schedule.run_pending()
    time.sleep(1)
