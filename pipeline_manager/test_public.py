from pipeline_manager import pipeline


def test_example() -> None:
    register = pipeline()

    answer = []

    @register
    def step1():
        answer.append(1)

    @register(depends_on=["step1"])
    def step2():
        answer.append(2)

    @register(depends_on=["step1", "step2"])
    def step3():
        answer.append(3)
    step3()
    assert answer == [1, 1, 2, 3]
