import allure
import pytest

from base.api.questions_api import QuestionsClient
from models.questions import DefaultQuestionsList, DefaultQuestion
from utils.assertions.assertions_functions import assert_status_code, assert_question
from utils.assertions.validate_schema import validate_schema


@pytest.mark.questions
@allure.feature('Questions')
@allure.story('Questions API')
class TestQuestions:
    @allure.title('Get all questions')
    def test_get_questions(self, class_questions_client: QuestionsClient):
        response = class_questions_client.get_all_questions_api()
        json_response = response.json()

        assert_status_code(response, 200)

        validate_schema(
            json_response, DefaultQuestionsList.model_json_schema())

    @allure.title('Get question by id')
    def test_get_question_by_id(self,
                                function_question: DefaultQuestion,
                                class_questions_client: QuestionsClient):
        response = class_questions_client.get_question_by_id_api(function_question.id)
        json_response = response.json()

        assert_status_code(response, 200)
        assert_question(
            expected_question=json_response,
            actual_question=function_question
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Create new question')
    def test_create_new_question_api(self, class_questions_client: QuestionsClient):
        payload = DefaultQuestion()

        response = class_questions_client.create_question_api(payload)
        json_response = response.json()

        assert_status_code(response, 201)
        assert_question(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

