import winsound
import time

Scale_Frequency = {'C3':130, 'C#3':138, 'D3':146, 'D#3':155, 
                   'E3':164, 'F3':174, 'F#3':185,'G3':196, 
                   'G#3':207, 'A3':220, 'A#3':238, 'B3':246,
                   'C4':261, 'C#4':277, 'D4':293, 'D#':311, 
                   'E4':329, 'F4':349, 'F#4':369,'G4':392, 
                   'G#4':415, 'A4':440, 'A#4':466, 'B4':493,
                   'C5':523, 'C#5':554, 'D5':587, 'D#5':622, 
                   'E5':659, 'F5':698, 'F#5':739,'G5':789, 
                   'G#5':830, 'A5':880, 'A#5':932, 'B5':987, 'C6':1046}

def note(pitch, duration):
    winsound.Beep(frequency=Scale_Frequency[pitch], duration=duration)


    
def HBD_Song():
    print('생일 축하~ 합니다~~')
    note('C5', 300)
    note('C5', 300)
    note('D5', 600)
    note('C5', 600)
    note('F5', 800)
    note('E5', 600)
    print()
    time.sleep(0.5)

    print('생일 축하~ 합니다~~')
    note('C5', 300)
    note('C5', 300)
    note('D5', 600)
    note('C5', 600)
    note('G5', 800)
    note('F5', 600)
    print()
    time.sleep(0.5)

    print('사랑하는...', name)
    note('C5', 300)
    note('C5', 300)
    note('C6', 1000)
    note('A5', 800)
    note('F5', 800)
    note('E5', 800)
    note('D5', 1000)
    print()
    time.sleep(1)

    print('생~~일~~ 축하~~~~~~ 합니다!')
    note('A#5', 400)
    note('A#5', 600)
    note('A5', 800)
    note('F5', 700)
    note('G5', 1700)
    note('F5', 300)
    print()
    
    print('짝짝짝짝짝짝짝')
    time.sleep(10)
    
name = input('이름을 입력해주세요.(글자가 안 보인다면 스페이스 한번!) \n>>')
print()
time.sleep(1)

print('처..')
time.sleep(1)
print('리..')
time.sleep(1)
print('중..')
print()
time.sleep(2)

print(name,'의 주변 지인들에게 자동으로 파티 초대 메세지를 전송 했습니다!')
print()
time.sleep(2)

print('농담입니다..ㅎ')
print()
time.sleep(1)

print('5초의 시간 동안 이어폰을 연결하거나 소리를 적정량으로 줄여주세요^^')
print()
time.sleep(5)

print('자~~~~')
print()
time.sleep(2)

HBD_Song()
