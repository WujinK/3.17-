# pip install seaborn
# pip install numpy
# pip install pandas
# pip install matplotlib
'''
countplot => 흔히 알고 있는 막대 그래프 // 기존에 존재하는 데이터 프레임을 대상으로 시각화
displot (함수임) => 구간별로 밀도 표현 가능 , 데이터의 전반적인 분포를 파악하는데 좋다.
heat map => 아름다운 시각화 장점이 가장 잘 드러나는 그래프
pairplot => 컬럼 간의 상관관계를 가늠해보는데 유용
violinplot => 컬럼에 대한 데이터 비교분포를 표현할 때 유용
lmplot => 산점도와 추세ㅔ선이 한 번에 합쳐진 그래프
jointplot => 산점도와 분포를 동시에 그려주는 그래프, 그래프의 종류 지정 가능 (모두 연속적인 실수인 데이터 일 때)
stripplot => 모든 데이터를 점으로 시각화

iris => 붓꽃데이터
titanic => 타이타닉호 데이터
tips => 팁
flights => 항공데이터

linspace => 수평축, 간격 만들 때 유용함
np.linespace(start,stop,num(step))

데이터 변수가 여러 개인 다차원 데이터는 데이터 종류에 따라 경우가 다름
1) 분석하고자 하는 데이터가 모두 실수인 경우
2) 분석하고자 하는 데이터가 모두 카테고리 값인 경우
3) 분석하고자 하는 데이터가 모두 실수 값과 카테고리 값이 섞여있는 경우
'''

'''
====seaborn====
darkdrid, whitegrid, dark, white, ticks
'''
