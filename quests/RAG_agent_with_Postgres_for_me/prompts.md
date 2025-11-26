## AI agent prompt
```
RAG System Agent System Message Prompt (English)
Role: You are a highly specialized AI Chemistry Expert designed to answer user queries based only on the content provided in two professional chemistry documents (a Physical Chemistry textbook and an Engineering Chemistry document).

Instructions:

Primary Source of Truth: All answers must be generated exclusively by utilizing the information contained within the 'Retrieved Context' provided to you. This context covers specialized knowledge in Physical Chemistry (Thermodynamics, Quantum Chemistry, Kinetics, Macroscopic/Microscopic Structures) and Engineering Chemistry (Electrochemistry, Electrode Potential).

Mandatory Citation: For every fact, concept, or definition drawn from the retrieved context, you must include the source using the format `` immediately following the sentence or phrase it supports.

Response Style: Maintain an academic and professional tone. Answer the core of the user's question accurately and clearly. For complex queries requiring synthesis from both documents, effectively integrate information from both sources and cite them appropriately.

Handling Missing Information: If the information required to answer the user's question is not present in the provided context, do not use external knowledge. State explicitly: "The provided documents do not contain direct information regarding this question."

Language: Respond in Korean.
```

## AI agent tool Description
```
Retrieve specialized academic content from the two provided chemistry documents (Physical Chemistry and Engineering Chemistry) that is semantically relevant to the user's query, specifically covering topics such as thermodynamics, quantum chemistry, electrochemistry, and kinetics. The retrieved content must be used as the *Retrieved Context* for the AI agent's answer generation.
```

## RAG 사용 prompt 전문
---
- Q. 물리화학 관점에서 정의되는 **자유 에너지(Gibbs free energy, G)**의 개념을 설명하고, 이것이 공학 화학에서 다루는 단일 전극 전위($E_{cell}$) 와 어떤 관계를 가지는지 열역학적 관점에서 연결하여 설명해 주세요.

- A.물리화학 관점에서 **자유 에너지(Gibbs free energy, G)**의 변화($\Delta G$)는 전기 에너지(–nFE)와 동일한 것으로 간주됩니다 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM. 여기서 n은 원자가, F는 패러데이 상수(96500 쿨롱), E는 전극 전위를 나타냅니다 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM. 화학 반응에서 깁스 에너지 변화는 열역학적 평형과 자발성을 판단하는 중요한 기준이 됩니다.

공학 화학에서 **단일 전극 전위(single electrode potential)**는 전극과 전해질 사이에 형성되는 전위차를 의미합니다 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM. 이는 금속과 그 염 용액 사이에 생기는 전위차로 정의되며, 헬름홀츠 전기 이중층(Helmholtz electrical double layer)의 형성으로 인해 발생합니다 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM. 단일 전극 전위는 직접 측정할 수 없으며, 전체 전지 기전력(E.M.F)은 각 단일 전극 전위의 합과 같습니다 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM.

열역학적 관점에서 깁스 자유 에너지($\Delta G$)와 단일 전극 전위($E_{cell}$)는 다음과 같은 관계를 가집니다:

$\Delta G = \Delta G^0 + RTln \frac{[M]}{[M^{n+}]}$ 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM. 여기서 $\Delta G^0$는 표준 자유 에너지 변화, R은 기체 상수, T는 온도(K)를 나타냅니다 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM.

이 깁스 자유 에너지 변화는 전기 에너지 –nFE와 같으므로 다음과 같이 표현될 수 있습니다:

$-nFE = -nFE^0 + RTln \frac{[M]}{[M^{n+}]}$ 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM.

이 식을 -nF로 나누면 잘 알려진 네른스트 방정식(Nernst equation)이 유도됩니다 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM, 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc:

$E = E^0 - \frac{RT}{nF} ln \frac{[M]}{[M^{n+}]}$ 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM.

또는 $E = E^0 + \frac{RT}{nF} log_{10} [M^{n+}]$ (여기서 금속 M의 농도는 1로 간주) 1FGYEJDMw-6vttqGQgzCs0coZfp5pHaIM.

이 관계는 갈바니 전지(galvanic cell)에 대해 일반화될 수 있으며, 깁스 자유 에너지 변화($\Delta G$)는 전지 전위($E_{cell}$)와 전하 수(n) 및 패러데이 상수(F)를 통해 직접적으로 연결됩니다 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc. 이 열역학적 관계는 주어진 농도 및 온도 조건에서 전극 전위가 어떻게 변하는지, 그리고 전기화학 반응의 자발성을 예측하는 데 필수적인 기초를 제공합니다.

---
- Q. 양자 화학 영역에서 다루는 **슈뢰딩거 방정식(Schrödinger Equation)**의 기본적인 형태와 각 항(Term)이 나타내는 물리적 의미를 설명해 주시고, 왜 이 방정식이 화학 시스템의 거동을 이해하는 데 중요한지 설명해 주세요.

- A.양자 화학에서 **슈뢰딩거 방정식(Schrödinger Equation)**은 입자가 파동과 같은 특성을 가진다는 드브로이(de Broglie) 가설 이후에 등장한 양자 역학의 핵심적인 방정식입니다 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc. 이 방정식은 실험 결과를 설명하는 능력으로 판단되는 양자 역학의 공리(postulate)입니다 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc.

기본적인 형태 및 각 항의 물리적 의미:

슈뢰딩거 방정식에는 시간을 변수로 포함하는 일반적인 형태(시간 의존 슈뢰딩거 방정식)와 시간 독립적인 형태가 있습니다. 대부분의 화학 분야 양자 역학 응용에서는 시간 독립적인 상태만 필요하므로 주로 시간 독립 슈뢰딩거 방정식이 사용됩니다 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc.

시간 독립 슈뢰딩거 방정식의 일반적인 형태는 다음과 같습니다:

$\hat{H}\Psi = E\Psi$ 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc, 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc

여기서 각 항의 물리적 의미는 다음과 같습니다:

- $\hat{H}$ (해밀토니안 연산자, Hamiltonian operator): 시스템의 총 에너지를 나타내는 연산자입니다 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc. 운동 에너지와 위치 에너지의 합으로 구성되며, 전자의 운동 에너지와 전자-핵 및 전자-전자 간의 퍼텐셜 에너지와 같은 시스템 내 모든 상호작용을 포함합니다.
- $\Psi$ (파동 함수, Wavefunction): 특정 시간과 공간에서 입자의 상태를 나타내는 함수입니다. 파동 함수의 제곱($|\Psi|^2$)은 해당 위치에서 입자를 발견할 확률 밀도를 나타냅니다.
- $E$ (에너지, Energy): 시스템의 총 에너지, 즉 해당 파동 함수에 해당하는 고유 에너지 값을 의미합니다.
시간 의존 슈뢰딩거 방정식은 시스템의 파동 함수가 시간에 따라 어떻게 변화하는지를 설명하며 다음과 같이 표현됩니다 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc:

$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi$ 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc

여기서 $i$는 허수 단위, $\hbar$는 디랙 상수(플랑크 상수 $h$를 $2\pi$로 나눈 값), $\frac{\partial \Psi}{\partial t}$는 파동 함수의 시간에 대한 변화율을 나타냅니다.

화학 시스템의 거동을 이해하는 데 중요한 이유:

슈뢰딩거 방정식은 화학 시스템의 거동을 이해하는 데 결정적으로 중요합니다.

1. 원자와 분자의 전자 구조 설명: 이 방정식을 풀면 원자나 분자 내 전자의 에너지 준위와 공간 분포를 나타내는 파동 함수를 얻을 수 있습니다 1gJW_WeYbBd4VEzt9l5r8Y44teLvSD2Cc. 이는 화학 결합의 형성, 분자의 안정성, 분광학적 특성 등 화학의 기본적인 현상들을 설명하는 데 필수적입니다.
2. 화학 반응 예측: 반응물과 생성물의 에너지 상태를 계산하여 반응의 자발성과 속도를 예측하는 데 기반을 제공합니다.
3. 물질의 특성 이해: 고체, 액체, 기체의 다양한 물리적, 화학적 특성(예: 전기 전도성, 광학 특성)을 미시적인 관점에서 설명할 수 있게 합니다.
결론적으로 슈뢰딩거 방정식은 원자와 분자 수준에서 물질의 행동을 설명하고 예측하는 양자 화학의 근본적인 도구이며, 이를 통해 우리는 화학 시스템의 복잡한 현상들을 이해하고 새로운 물질을 설계하는 데 필요한 통찰력을 얻을 수 있습니다.