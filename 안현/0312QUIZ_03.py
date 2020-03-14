"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""
import random
input('1p의 주사위를 엔터키를 눌러 던져주세요')
output1p = random.randrange(1,7)
input('2p의 주사위를 엔터키를 눌러 던져주세요')
output2p = random.randrange(1,7)
if output1p>output2p:
    print('첫 번째 플레이어가 {}, 두 번째 플레이어가 {}를 주사위의 눈으로 얻어, 첫 번째 플레이어가 승리했습니다'. format(output1p, output2p))
elif output1p<output2p:
    print('첫 번째 플레이어가 {}, 두 번째 플레이어가 {}를 주사위의 눈으로 얻어, 두 번째 플레이어가 승리했습니다'. format(output1p, output2p))
else :
    print('첫 번째 플레이어가 {}, 두 번째 플레이어가 {}를 주사위의 눈으로 얻어 무승부가 되었습니다.' . format(output1p, output2p))
