import allure

from models.questions import DefaultQuestion, QuestionDict, UpdateQuestion


@allure.step('Validating status code')
def assert_status_code(response, expected_code):
    with allure.step(f'Checking that {response.status_code} equals to {expected_code}'):
        assert response.status_code == expected_code


def assert_post(
        expected_question: QuestionDict,
        actual_question: DefaultQuestion | UpdateQuestion
):
    if isinstance(actual_question, DefaultQuestion):
        with allure.step(f'Checking that "Question id" equals to {actual_question.id}'):
            assert (expected_question["id"]) == actual_question.id

    with allure.step(f'Checking that "Question "question" equals to {actual_question.question}'):
        assert (expected_question["question"]) == actual_question.user_id

    with allure.step(f'Checking that "Question possibleAnswers" equals to {actual_question.possible_answers}'):
        assert (expected_question["possibleAnswers"]) == actual_question.possible_answers

    with allure.step(f'Checking that "Question correctAnswers" equals to {actual_question.correct_answer}'):
        assert (expected_question["correctAnswers"]) == actual_question.correct_answer
