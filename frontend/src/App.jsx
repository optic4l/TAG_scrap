import React from 'react'
import { useState } from 'react'

const App = () => {

  const [patente, setPatente] = useState('')
  const [userId, setUserId] = useState('')

  const  enviarDatos = async () => {
    await fetch('http://localhost:8000/scrape/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_id: userId,
        patente: patente,
      }),
    })
  }

  return (
    <div>
      <h1>Pasaste sin TAG scraper</h1>
      <p>¡Bienvenido a la aplicación!</p>
      <form >
        <label htmlFor="patenteInput">Ingresa la patente:</label>
        <input type="text" id="patenteInput" name="patenteInput" value={patente} onChange={e => setPatente(e.target.value)}/>
        
        <label htmlFor="userIdInput">Ingrese su id de usuario tlg:</label>
        <input type="text" id="userIdInput" name="userIdInput" value={userId} onChange={e => setUserId(e.target.value)}/>
     
        <button type="submit" onClick={enviarDatos}>Enviar</button>
      </form>
    </div>
  )
}

export default App