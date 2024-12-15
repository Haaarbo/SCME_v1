import { useState } from "react";
import CadUsuario from "../forms/CadUsuario";
import CadMaterial from "../forms/CadMaterial";
import "../styles/Cadastro.css";  // Caminho relativo para importar o arquivo de estilo

function Cadastro(){
    const [tipoCadastro, setTipoCadastro] = useState(null);

    return(
        <div className="cadastro-container">
  <h1>Cadastro</h1>
  
  <div className="button-container">
    <button onClick={() => setTipoCadastro("usuario")}>Cadastrar Usuário</button>
    <button onClick={() => setTipoCadastro("material")}>Cadastrar Material</button>
  </div>

  {tipoCadastro === "usuario" && <CadUsuario />}
  {tipoCadastro === "material" && <CadMaterial />}
</div>

    )
}

export default Cadastro;