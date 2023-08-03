1.Перейти на сайт https://forhemer.github.io/React-Todo-List/



describe('Todo List Test', () => {
  it('should visit the Todo List website', () => {
    cy.visit('https://forhemer.github.io/React-Todo-List/') 
 })
})


 2. Добавить поочерёдно 3 элемента в ToDo лист

describe('Todo List Test', () => {
  it('should visit the Todo List website and add items', () => {
    cy.visit('https://forhemer.github.io/React-Todo-List/')

    cy.get('.new-todo')
      .type('Item 1{enter}')
      .type('Item 2{enter}')
      .type('Item 3{enter}')
  })
})

3.Проверить, что элементов в листе стало действительно 3

describe('Todo List Test', () => {
  it('should visit the Todo List website, add items, and check their count', () => {
    cy.visit('https://forhemer.github.io/React-Todo-List/')

    cy.get('.new-todo')
      .type('Item 1{enter}')
      .type('Item 2{enter}')
      .type('Item 3{enter}')

    cy.get('.todo-list li').should('have.length', 3)
  })
})

4.Пометить один из элементов как выполненный (галочкой в чекбоксе)

describe('Todo List Test', () => {
  it('should visit the Todo List website, add items, mark one item as completed', () => {

    cy.visit('https://forhemer.github.io/React-Todo-List/')

    cy.get('.new-todo')
      .type('Item 1{enter}')
      .type('Item 2{enter}')
      .type('Item 3{enter}')

    cy.get('.toggle').first().click()
  })
})

5.Проверить, что текст этого элемента стал зачёркнутым

describe('Todo List Test', () => {
  it('should visit the Todo List website, add items, mark one item as completed, and check its text decoration', () => {

    cy.visit('https://forhemer.github.io/React-Todo-List/')

    cy.get('.new-todo')
      .type('Item 1{enter}')
      .type('Item 2{enter}')
      .type('Item 3{enter}')

    cy.get('.toggle').first().click()

    cy.get('.todo-list li').first().should('have.css', 'text-decoration', 'line-through')

  })
})

6.7.Удалить элемент из списка и проверить, что элемент больше не отображается в списке

describe('Todo List Test', () => {
  it('should visit the Todo List website, add items, delete one item, and verify its absence', () => {

    cy.visit('https://forhemer.github.io/React-Todo-List/')

    cy.get('.new-todo')
      .type('Item 1{enter}')
      .type('Item 2{enter}')
      .type('Item 3{enter}')

    cy.get('.destroy').eq(1).click()

    cy.get('.todo-list li').should('have.length', 2)
    cy.contains('.todo-list li', 'Item 2').should('not.exist')

  })
})
