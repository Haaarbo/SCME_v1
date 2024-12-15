import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000, // Porta configurada no docker-compose.yml
    host: "0.0.0.0", // Permitir acesso externo pelo Docker
  },
});
