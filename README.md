# Exercice - Create a blog tool using a tdd-like approach

## Goals

With this exercice, i hope you will learn these skills : 
* understanding MVC pattern with OOP
* develop something following tests (that is a part of TDD, but you don't write the tests).

## Prerequisite
* Python
* [Pytest](https://docs.pytest.org/en/latest/) 

## Exercice 1 - create the controller
* Download the file test_blog.py.
* Comments every line
* Uncomment the first lines (1 to 6). It includes the imports, the function test_should_select_model and the first assert
* Run the test (Red step)
* Add the code to pass the first test (Green step)
* Uncomment the next assert, and do RED - GREEN step.
* Uncomment the next test_* function until the end
* When needing, do refactoring

In this exercice, NEVER CHANGE THE TESTS. You can only comment / uncomment the code.

When you have a controller and a model_in_memory working, you can go the the next Exercice

## Exercice 2 (optional) - create the delete functionnality
Following the same principle of the first exercice, you have to create the function delete_article.

Follow this steps : 
* RED - write a test which fails
* GREEN - make this test pass
* REFACTORING - clean your code (remove duplication, rename variable, etc...)

## Exercice 3 - create the real model
For the next exercice, you have to create a model which has the same interface than the ModelInMemory class.
You can use pytest to make some integration test.
You will test each method of the class. Don't forget to test the error.

To do that, you can use any database. I suggest you to use an orm and do your test with a sqlite database in memory. This way, you can ignore the tear_down step of test (you don't have to clean the database after each test).

When you have a model working, you can go to the next Exercice

## Exercice 4 - create the view (terminal)
In this exercice, you have to create a view to use the controller and the last model you wrote. This view should work in the terminal.

## Exercice 5 - create the view (web based)
Like the same exercice, but you have to write a web based application.
You can use frameworks like [bottlepy](https://bottlepy.org/docs/dev/), [flask](https://www.palletsprojects.com/p/flask/), etc...

