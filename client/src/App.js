import React, { useState, useEffect } from 'react'
import request from './axios/axios'

function App() {
  const [cards, setCards] = useState([{}])

  const getAndSetCards = () => {
    request.get('/chase/cards')
      .then(({ data }) => setCards(data))
  }

  useEffect(() => {
    getAndSetCards() 
  }, [])

  console.log(cards)
  return (
    <div>{cards.map((card) => {
      return <div>{card.name}</div>
    })}</div>
  )
}

export default App