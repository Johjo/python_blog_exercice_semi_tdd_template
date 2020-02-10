# Exercice - Create a blog tool using a tdd-like approach

## Goals

With this exercice, i hope you will learn these skills : 
* understanding MVC pattern with OOP
* develop something following tests (that is a part of TDD, but you don't write the tests).

## Prerequisite
* Python
* [Pytest](https://docs.pytest.org/en/latest/) 

## First exercice - create the controller
* Download the file test_blog.py.
* Comments every line
* Uncomment the first lines (1 to 6). It includes the imports, the function test_should_select_model and the first assert
* Run the test (Red step)
* Add the code to pass the first test (Green step)
* Uncomment the next assert, and do RED - GREEN step.
* Uncomment the next test_* function until the end
* When needing, do refactoring

When you have a controller and a model_in_memory working, you can go the the next Exercice

## Second exercice - create the real model
For the next exercice, you have to create a model which has the same interface than the ModelInMemory class.
You can use pytest to make some integration test.
You will test each method of the class. Don't forget to test the error.

To do that, you can use any database. I suggest you to use an orm and do your test with a sqlite database in memory. This way, you can ignore the tear_down step of test (you don't have to clean the database after each test).

When you have a model working, you can go to the next Exercice

