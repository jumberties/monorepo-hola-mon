import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [message, setMessage] = useState('Carregant...')

  useEffect(() => {
    axios.get('/api/message')
      .then(res => setMessage(res.data.message))
      .catch(() => setMessage('Error connectant amb el backend'))
  }, [])

  return (
    <div style={{ textAlign: 'center', marginTop: '4rem' }}>
      <h1>React + FastAPI + PostgreSQL</h1>
      <p>{message}</p>
    </div>
  )
}

export default App

