import React, { useState } from 'react';

const Pesquisa = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const response = await fetch(`http://localhost:8000/api/search_materials/?query=${query}`);
    const data = await response.json();
    setResults(data);  // Atualiza o estado com os resultados
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}  // Atualiza o estado com a pesquisa
        placeholder="Digite para pesquisar"
      />
      <button onClick={handleSearch}>Pesquisar</button>

      <ul>
        {results.map((result, index) => (
          <li key={index}>
            {result.nome} - {result.serial}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Pesquisa;
