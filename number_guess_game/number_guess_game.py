GAME_TITLE_MAX_LEN      = 28
GAME_TITLE_START_PROMPT = f'게임 제목을 입력해 주세요. (최대 {GAME_TITLE_MAX_LEN}자이내(<={GAME_TITLE_MAX_LEN}), 반드시 영문 or 숫자 만 사용 가능)'
GAME_TITLE_ERROR_MSG    = '정확하게 입력하세요'
end_msg = '게임을 종료합니다'
while True:
  # 2-1. 사용자 입력 대기
  game_title = input( GAME_TITLE_START_PROMPT + "\n" ).strip() # 양쪽 공백 제거 수행

  if not game_title: # 2-2-1. 입력값이 없다면 (그냥 엔터, 공백만 넣고 엔터)
    print( GAME_TITLE_ERROR_MSG )
  elif len(game_title) > GAME_TITLE_MAX_LEN:  # 2-2-2. 28자 초과
    print( GAME_TITLE_ERROR_MSG ) # 리뷰때 초과된 글자수를 표현하여 에러 메시지 수정
  else:              # 2-2-3. 정상
    # 2-2-3-1. 탈출코드 : 정확하게 입력했다면
    break

PLAYER_MAX_LEN      = GAME_TITLE_MAX_LEN 
PLAYER_START_PROMPT = f'플레이어의 이름을 입력해 주세요. (최대 {PLAYER_MAX_LEN}자이내(<={PLAYER_MAX_LEN}), 반드시 영문 or 숫자 만 사용 가능)'

while True:
  player_name = input( PLAYER_START_PROMPT + "\n" ).strip()
  if not player_name:
    print( GAME_TITLE_ERROR_MSG )
    continue # 하위 코드 실행 x, 나를 감싸고 있는 가장 가까운 반복문의 조건식으로 점프

  if len(player_name) > PLAYER_MAX_LEN:
    print( GAME_TITLE_ERROR_MSG )
    continue # 하위 코드 실행 x, 나를 감싸고 있는 가장 가까운 반복문의 조건식으로 점프

  # 코드가 실행하는 부분이 여기까지 도착했다 => 정상입력했음을 의미하는 것임
  break # 탈출


GAME_INTRO_AROUND_ICON = '*'
GAME_INTRO_CHAR_SPACE  = GAME_TITLE_MAX_LEN + 2 # 30, 2는 앞뒤 경계 각각 칸수총합

print(GAME_INTRO_AROUND_ICON * GAME_INTRO_CHAR_SPACE)
print(f'{GAME_INTRO_AROUND_ICON}{game_title:^28}{GAME_INTRO_AROUND_ICON}')
print(f'{GAME_INTRO_AROUND_ICON}{player_name:^28}{GAME_INTRO_AROUND_ICON}')
print(f'{GAME_INTRO_AROUND_ICON}{'press any key':^28}{GAME_INTRO_AROUND_ICON}')
print(GAME_INTRO_AROUND_ICON * GAME_INTRO_CHAR_SPACE)

import random



GAME_RANGE_ERROR_MSG='유효 범위값만 입력됩니다'
yes_list=['yes', 'Yes', 'Y', 'y', 'yEs', 'yeS', 'YES']
no_list=['No','no', 'nO', 'NO','n','N']
Max_score=100
minus_score=10
while True:
  input_number =0
  ai_number = random.randint( 1, 100 )
  score = Max_score
  trial=0
  print("AI가 생성한 값 1 ~ 100 사이중 하나의 정수값을 맞추시오")
  while input_number != ai_number:
    input_number =int(input())
    if input_number > 100 or input_number<1 :
      print(GAME_RANGE_ERROR_MSG)
      continue
    trial+=1
    if ai_number > input_number :
      score-=minus_score
      print(f'{trial}{'번째 시도입니다'}')
      print("힌트 : 더 큰 숫자입니다")

    elif ai_number < input_number :
      score-=minus_score
      print(f'{trial}{'번째 시도입니다'}')
      print("힌트: 더 작은 숫자입니다")
  print(f'{trial}{'번째 시도입니다'}')
  print("정답입니다")
  print(f'{score}{'점입니다!!'}')
  print('다시 게임을 하시겠습니까?')
  answer=input()
  if answer in yes_list :
    continue
  elif answer in no_list :
    print(f'{end_msg}')
    break
  break

