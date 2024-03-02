import allure
from requests import Response

from client.api_client import ApiClient
from models.questions import DefaultQuestion, UpdateQuestion
from utils.constants.routes import APIRoutes


class QuestionsClient(ApiClient):
    @allure.step('Getting all questions')
    def get_all_questions_api(self) -> Response:
        return self.client.request('GET', APIRoutes.QUESTIONS)

    @allure.step('Getting question with id "{question_id}"')
    def get_question_by_id_api(self, question_id: int):
        return self.client.request('GET', f'{APIRoutes.QUESTIONS}/{question_id}')

    @allure.step('Creating question')
    def create_question_api(self, payload: DefaultQuestion):
        return self.client.request('POST',
                                   APIRoutes.QUESTIONS,
                                   json=payload.model_dump(by_alias=True))

    @allure.step('Updating question with id "{question_id}"')
    def update_question_api(self, question_id: int, payload: UpdateQuestion):
        return self.client.request('PATCH',
                                   f'{APIRoutes.QUESTIONS}/{question_id}',
                                   json=payload.model_dump(by_alias=True))

    @allure.step('Deleting question with id "{question_id}"')
    def delete_question_api(self, question_id: int):
        return self.client.request('DELETE', f'{APIRoutes.QUESTIONS}/{question_id}')

    def create_question(self) -> DefaultQuestion:
        payload = DefaultQuestion()
        response = self.create_question_api(payload)
        return DefaultQuestion(**response.json())

