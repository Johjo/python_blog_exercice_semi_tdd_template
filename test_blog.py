import pytest

from controller import Controller

def test_should_select_model():
    assert_create_controller_with_model(ModelInMemory(articles=[]), "Controller ( model : inmemory )")
    assert_create_controller_with_model(ModelInMemory1(), "Controller ( model : inmemory1 )")
    assert_create_controller_with_model(ModelInMemory2(), "Controller ( model : inmemory2 )")


def assert_create_controller_with_model(model, expected_str):
    controller = Controller(model)
    assert str(controller) == expected_str


@pytest.fixture
def model_with_one_article():
    return Controller(ModelInMemory([Article(title="title 1", text="text 1")]))


@pytest.fixture
def model_with_two_articles():
    return Controller(ModelInMemory([Article(title="title 1", text="text 1"), Article(title="title 2", text="text 2")]))


def test_should_list_one_article(model_with_one_article):
    controller = Controller(model_with_one_article)
    articles = controller.get_all_articles()
    assert len(articles) == 1
    assert articles[0].get_title() == "title 1"
    assert articles[0].get_text() == "text 1"


def test_should_list_two_article(model_with_two_articles):
    controller = Controller(model_with_two_articles)
    articles = controller.get_all_articles()
    assert len(articles) == 2
    assert articles[0].get_title() == "title 1"
    assert articles[0].get_text() == "text 1"

    assert articles[1].get_title() == "title 2"
    assert articles[1].get_text() == "text 2"


def test_should_update_article(model_with_two_articles):
    controller = Controller(model_with_two_articles)
    controller.update_article(title="title 1", new_text="new text 1")
    articles = controller.get_all_articles()
    assert len(articles) == 2
    assert articles[0].get_title() == "title 1"
    assert articles[0].get_text() == "new text 1"

    assert articles[1].get_title() == "title 2"
    assert articles[1].get_text() == "text 2"


def test_should_create_article(model_with_two_articles):
    controller = Controller(model_with_two_articles)
    controller.create_article(title="title 3", text="text 3")

    articles = controller.get_all_articles()
    assert len(articles) == 3
    assert articles[0].get_title() == "title 1"
    assert articles[0].get_text() == "text 1"

    assert articles[1].get_title() == "title 2"
    assert articles[1].get_text() == "text 2"

    assert articles[2].get_title() == "title 3"
    assert articles[2].get_text() == "text 3"


def test_should_send_error_when_new_article_already_exist(model_with_two_articles):
    controller = Controller(model_with_two_articles)
    assert_raise_error_when_article_already_exists(controller,
                                                   new_title="title 2",
                                                   expected_error="Article 'title 2' already exists")
    assert_raise_error_when_article_already_exists(controller,
                                                   new_title="title 1",
                                                   expected_error="Article 'title 1' already exists")


def assert_raise_error_when_article_already_exists(controller, expected_error, new_title):
    try:
        controller.create_article(title=new_title, text="some text")
        pytest.fail("Exception was expected")
    except ArticleAlreadyExistException as e:
        assert e.message == expected_error


class NonExistantArticleException(Exception):
    def __init__(self, message):
        self.message = message


def test_should_raise_error_when_updating_nonexistant_article(model_with_two_articles):
    controller = Controller(model_with_two_articles)
    assert_raise_error_when_updating_nonexistant_article(controller,
                                                         expected_error="Article 'title unknown 1' does not exist",
                                                         updated_title="title unknown 1")

    assert_raise_error_when_updating_nonexistant_article(controller,
                                                         expected_error="Article 'title unknown 2' does not exist",
                                                         updated_title="title unknown 2")


def assert_raise_error_when_updating_nonexistant_article(controller, expected_error, updated_title):
    try:
        controller.update_article(title=updated_title, new_text="some text")
        pytest.fail("Exception was expected")
    except NonExistantArticleException as e:
        assert e.message == expected_error
