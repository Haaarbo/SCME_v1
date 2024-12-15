import React, { useState } from "react";
import "../styles/Cadastro.css";

function CadUsuario() {
  const [formData, setFormData] = useState({
    nome: "",
    email: "",
    cpf: "",
    funcao: "",
  });

  const [formErrors, setFormErrors] = useState({});
  const [successMessage, setSuccessMessage] = useState("");

  const validate = () => {
    const errors = {};
    if (!formData.nome.trim()) errors.nome = "O nome é obrigatório.";
    if (!formData.email.trim()) {
      errors.email = "O e-mail é obrigatório.";
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      errors.email = "Insira um e-mail válido.";
    }
    if (!formData.cpf.trim()) {
      errors.cpf = "O CPF é obrigatório.";
    } else if (!/^\d{3}\.\d{3}\.\d{3}-\d{2}$/.test(formData.cpf)) {
      errors.cpf = "Insira um CPF válido no formato XXX.XXX.XXX-XX.";
    }
    if (!formData.funcao) errors.funcao = "Selecione uma função.";
    return errors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = validate();
    if (Object.keys(errors).length > 0) {
        setFormErrors(errors);
        setSuccessMessage("");
    } else {
        setFormErrors({});
        setSuccessMessage("Usuário cadastrado com sucesso!");

        const response = await fetch('http://localhost:8000/api/usuarios/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Usuário criado:", data);
        } else {
            console.error("Erro ao criar usuário");
        }
    }
};

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <div className="form-container">
      <h2>Cadastro de Usuário</h2>
      {successMessage && <p className="success-message">{successMessage}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="nome">Nome:</label>
          <input
            type="text"
            id="nome"
            name="nome"
            placeholder="Insira um nome"
            value={formData.nome}
            onChange={handleChange}
          />
          {formErrors.nome && <span className="error">{formErrors.nome}</span>}
        </div>
        <div className="form-group">
          <label htmlFor="email">E-mail:</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="example@gmail.com"
            value={formData.email}
            onChange={handleChange}
          />
          {formErrors.email && (
            <span className="error">{formErrors.email}</span>
          )}
        </div>
        <div className="form-group">
          <label htmlFor="cpf">CPF:</label>
          <input
            type="text"
            id="cpf"
            name="cpf"
            placeholder="XXX.XXX.XXX-XX"
            value={formData.cpf}
            onChange={handleChange}
          />
          {formErrors.cpf && <span className="error">{formErrors.cpf}</span>}
        </div>
        <div className="form-group">
          <label htmlFor="funcao">Função:</label>
          <select
            id="funcao"
            name="funcao"
            value={formData.funcao}
            onChange={handleChange}
          >
            <option value="">Selecione</option>
            <option value="tecnico">Técnico</option>
            <option value="enfermagem">Enfermagem</option>
            <option value="administrativo">Administrativo</option>
          </select>
          {formErrors.funcao && (
            <span className="error">{formErrors.funcao}</span>
          )}
        </div>
        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
}

export default CadUsuario;
