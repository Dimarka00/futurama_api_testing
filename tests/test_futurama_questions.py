import allure
import pytest

from base.api.questions_api import QuestionsClient
from models.questions import DefaultQuestionsList, DefaultQuestion, UpdateQuestion
from utils.assertions.assertions_functions import assert_status_code, assert_question, assert_ids_is_equals, \
    assert_error_text
from utils.assertions.validate_schema import validate_schema


@pytest.mark.questions
@allure.feature('Questions')
@allure.story('Questions API')
class TestQuestions:
    """
    Tests for /questions
    """
    @allure.title('Get all questions')
    def test_get_questions(self, class_questions_client: QuestionsClient):
        """
        Get list of all questions with default params
        GET /questions
        """
        response = class_questions_client.get_all_questions_api()
        json_response = response.json()

        assert_status_code(response, 200)

        validate_schema(
            json_response, DefaultQuestionsList.model_json_schema())

    @allure.title('Get question with params')
    @pytest.mark.parametrize("param_id", [1, 2])
    def test_get_question_id_param(self, class_questions_client: QuestionsClient, param_id):
        """
        Get question by id e.g. 1, 2
        GET /questions
        """
        response = class_questions_client.get_all_questions_api(param_id)
        json_response = response.json()

        assert_status_code(response, 200)

        validate_schema(
            json_response, DefaultQuestionsList.model_json_schema())

    @allure.title('Get question by id')
    def test_get_question_by_id(self,
                                function_question: DefaultQuestion,
                                class_questions_client: QuestionsClient):
        """
        Get question by id
        GET /questions/{question_id}
        """
        response = class_questions_client.get_question_by_id_api(function_question.id)
        json_response = response.json()

        assert_status_code(response, 200)
        assert_question(
            expected_question=json_response,
            actual_question=function_question
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Get question by existing id')
    @pytest.mark.parametrize('question_id', [1, 3, 5])
    def test_get_question_by_existing_id(self, class_questions_client: QuestionsClient, question_id):
        """
        Get question by existing id, e.g. 1, 3, 5
        GET /questions/{question_id}
        """
        response = class_questions_client.get_question_by_id_api(question_id)
        json_response = response.json()

        assert_status_code(response, 200)
        assert_ids_is_equals(question_id, json_response["id"])

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Get question by not existing id')
    @pytest.mark.parametrize('question_id', [-854543, -343553, 0])
    def test_get_question_by_not_existing_id(self, class_questions_client: QuestionsClient, question_id):
        """
        Get question by not existing id, e.g. -854543, -343553, 0
        GET /questions/{question_id}
        """
        response = class_questions_client.get_question_by_id_api(question_id)

        assert_status_code(response, 404)
        assert response.json() == {}

    @allure.title('Create new question')
    def test_create_new_question_api(self, class_questions_client: QuestionsClient):
        """
        Create a new question
        POST /questions
        """
        payload = DefaultQuestion()

        response = class_questions_client.create_question_api(payload)
        json_response = response.json()

        assert_status_code(response, 201)
        assert_question(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Create a new question with empty body')
    @pytest.mark.xfail
    def test_create_new_question_with_empty_body_api(self, class_questions_client: QuestionsClient):
        """
        Create a new question with empty body
        POST /questions
        """
        payload = {}

        response = class_questions_client.create_question_api(payload)
        json_response = response.json()

        assert_status_code(response, 200)
        assert_error_text(json_response)

    @allure.title('Update question by id')
    def test_update_question_api(self,
                                 function_question: DefaultQuestion,
                                 class_questions_client: QuestionsClient):
        """
        Update an existing question by id
        PATCH /questions/{question_id}
        """
        payload = UpdateQuestion()

        response = class_questions_client.update_question_api(
            function_question.id, payload
        )
        json_response = response.json()

        assert_status_code(response, 400)
        assert_question(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Delete question by id')
    def test_delete_question_api(self,
                                 function_question: DefaultQuestion,
                                 class_questions_client: QuestionsClient):
        """
        Delete an existing question by id
        DELETE /questions/{question_id}
        """
        delete_question_response = class_questions_client.delete_question_api(
            function_question.id
        )
        get_question_response = class_questions_client.get_question_by_id_api(
            function_question.id
        )

        assert_status_code(delete_question_response, 200)
        assert_status_code(get_question_response, 404)
