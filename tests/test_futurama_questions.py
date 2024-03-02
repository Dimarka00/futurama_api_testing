import allure
import pytest

from base.api.questions_api import QuestionsClient
from models.questions import DefaultQuestionsList
from utils.assertions.assertions_functions import assert_status_code
from utils.assertions.validate_schema import validate_schema


@pytest.mark.questions
@allure.feature('Questions')
@allure.story('Questions API')
class TestQuestions:
    @allure.title('Get questions')
    def test_get_questions(self, class_questions_client: QuestionsClient):
        response = class_questions_client.get_all_questions_api()
        json_response = response.json()

        assert_status_code(response, 200)

        validate_schema(
            json_response, DefaultQuestionsList.model_json_schema())
