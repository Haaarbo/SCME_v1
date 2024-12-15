import React, { useState } from "react";
import "../styles/CadMaterial.css";

function CadMaterial() {
  const [nome, setNome] = useState("");
  const [serial, setSerial] = useState("");
  const [etapa, setEtapa] = useState("");
  const [erro, setErro] = useState(""); // Mensagem de erro

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validação simples
    if (!nome || !serial || !etapa) {
      setErro("Todos os campos devem ser preenchidos.");
      return;
    }

    // Validação do formato do serial (exemplo simples)
    const serialRegex = /^[A-Za-z0-9]+$/; // Permite apenas letras e números
    if (!serialRegex.test(serial)) {
      setErro("O serial deve conter apenas letras e números.");
      return;
    }

    // Validação do tamanho do nome do material
    if (nome.length < 3) {
      setErro("O nome do material deve ter pelo menos 3 caracteres.");
      return;
    }

    // Validação do tamanho do serial
    if (serial.length < 5) {
      setErro("O serial do material deve ter pelo menos 5 caracteres.");
      return;
    }

    const materialData = { nome, serial, etapa };

    const response = await fetch('http://localhost:8000/api/materiais/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(materialData),
    });

    if (response.ok) {
        const data = await response.json();
        console.log("Material cadastrado:", data);
        setErro(""); // Limpar erro
    } else {
        console.error("Erro ao cadastrar material");
    }

    setNome("");
    setSerial("");
    setEtapa("");
  };

  return (
    <div className="cad-material">
      <h2>Cadastro de Material</h2>
      {erro && <p className="error-message">{erro}</p>} {/* Exibição da mensagem de erro */}

      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="nome">Nome do Material</label>
          <input
            type="text"
            id="nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="serial">Serial</label>
          <input
            type="text"
            id="serial"
            value={serial}
            onChange={(e) => setSerial(e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="etapa">Selecione a Etapa</label>
          <select
            id="etapa"
            value={etapa}
            onChange={(e) => setEtapa(e.target.value)}
          >
            <option value="">Selecione...</option>
            <option value="recebimento">Recebimento</option>
            <option value="lavagem">Lavagem</option>
            <option value="esterilizacao">Esterilização</option>
            <option value="distribuicao">Distribuição</option>
          </select>
        </div>

        <button type="submit">Cadastrar Material</button>
      </form>
    </div>
  );
}

export default CadMaterial;
