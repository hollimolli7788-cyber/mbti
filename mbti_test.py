class PersonalityTest:
    def __init__(self):
        # 각 차원별 문항 리스트 (질문, [A유형 점수 방향, B유형 점수 방향])
        self.questions = [
            # 1. 외향(E) vs 내향(I)
            {
                "dimension": "EI",
                "q": "주말에 에너지를 충전하는 방식은?",
                "options": ["1. 친구들과 모임이나 파티에 참석한다 (E)", "2. 조용히 집에 혼자 쉬거나 책을 읽는다 (I)"],
                "weights": ("E", "I")
            },
            {
                "dimension": "EI",
                "q": "새로운 사람들을 만났을 때 나는?",
                "options": ["1. 먼저 쉽게 말을 건네고 대화를 주도한다 (E)", "2. 상대가 먼저 다가와 주기를 기다리는 편이다 (I)"],
                "weights": ("E", "I")
            },
            
            # 2. 감각(S) vs 직관(N)
            {
                "dimension": "SN",
                "q": "문제를 해결할 때 나는 주로 무엇을 신뢰하는가?",
                "options": ["1. 눈에 보이는 사실, 경험, 구체적인 데이터 (S)", "2. 직감, 가능성, 미래의 아이디어 (N)"],
                "weights": ("S", "N")
            },
            {
                "dimension": "SN",
                "q": "영화를 보거나 책을 읽을 때 나는?",
                "options": ["1. 있는 그대로의 스토리와 현실적인 묘사에 몰입한다 (S)", "2. 숨겨진 의미나 상징, 은유적 해석을 찾으려 한다 (N)"],
                "weights": ("S", "N")
            },
            
            # 3. 사고(T) vs 감정(F)
            {
                "dimension": "TF",
                "q": "친구가 고민을 털어놓으며 조언을 구할 때 나의 반응은?",
                "options": ["1. 객관적인 상황 분석과 해결책을 제시한다 (T)", "2. 먼저 공감하고 감정에 깊이 동조해 준다 (F)"],
                "weights": ("T", "F")
            },
            {
                "dimension": "TF",
                "q": "중대한 결정을 내릴 때 더 중요하게 생각하는 것은?",
                "options": ["1. 논리적 타당성과 효율성 (T)", "2. 주변 사람들의 감정과 조화 (F)"],
                "weights": ("T", "F")
            },
            
            # 4. 판단(J) vs 인식(P)
            {
                "dimension": "JP",
                "q": "여행을 떠날 때 나는?",
                "options": ["1. 일정표와 예산을 철저하게 미리 계획한다 (J)", "2. 대략적인 방향만 잡고 즉흥적으로 움직인다 (P)"],
                "weights": ("J", "P")
            },
            {
                "dimension": "JP",
                "q": "작업이나 과제를 처리할 때 나는?",
                "options": ["1. 마감일보다 훨씬 전에 미리 끝내놓는 편이다 (J)", "2. 마감 직전에 집중력이 폭발해 처리한다 (P)"],
                "weights": ("J", "P")
            }
        ]
        
        # 점수 집계 딕셔너리
        self.scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    def run_test(self):
        print("=" * 50)
        print("🧠 간단한 파이썬 성격유형(MBTI 스타일) 테스트에 오신 걸 환영합니다!")
        print("각 질문에 1번 또는 2번을 선택해주세요.")
        print("=" * 50 + "\n")

        for idx, item in enumerate(self.questions, 1):
            print(f"[질문 {idx}/{len(self.questions)}] {item['q']}")
            for opt in item["options"]:
                print(opt)
            
            while True:
                try:
                    choice = int(input("선택 (1 또는 2): "))
                    if choice in [1, 2]:
                        selected_trait = item["weights"][choice - 1]
                        self.scores[selected_trait] += 1
                        break
                    else:
                        print("⚠️ 1 또는 2만 입력해주세요.")
                except ValueError:
                    print("⚠️ 숫자로 입력해주세요.")
            print("-" * 50)

    def calculate_result(self):
        ei = "E" if self.scores["E"] >= self.scores["I"] else "I"
        sn = "S" if self.scores["S"] >= self.scores["N"] else "N"
        tf = "T" if self.scores["T"] >= self.scores["F"] else "F"
        jp = "J" if self.scores["J"] >= self.scores["P"] else "P"
        
        mbti_result = ei + sn + tf + jp
        
        print("\n" + "=" * 50)
        print("🎉 성격유형 테스트 결과 분석 완료!")
        print("=" * 50)
        print(f"당신의 성격 유형은 바로 **[ {mbti_result} ]** 입니다!\n")
        
        print("📊 세부 점수 분포:")
        print(f"- 외향(E): {self.scores['E']}점 vs 내향(I): {self.scores['I']}점")
        print(f"- 감각(S): {self.scores['S']}점 vs 직관(N): {self.scores['N']}점")
        print(f"- 사고(T): {self.scores['T']}점 vs 감정(F): {self.scores['F']}점")
        print(f"- 판단(J): {self.scores['J']}점 vs 인식(P): {self.scores['P']}점")
        print("=" * 50)

if __name__ == "__main__":
    test = PersonalityTest()
    test.run_test()
    test.calculate_result()
    