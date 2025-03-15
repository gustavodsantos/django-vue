import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useCursosStore = defineStore('cursos', () => {
  const cursos = ref([]);

  async function fetchCursos() {
    try {
      const response = await axios.get('/api/cursos/');
      console.log('Dados recebidos:', response.data);  // Verifique os dados no console
      cursos.value = response.data;  // Atualiza o estado da store
      console.log('Cursos na store:', cursos.value);  // Verifique se os dados foram atualizados
    } catch (error) {
      console.error('Erro ao buscar cursos:', error);
    }
  }

  return { cursos, fetchCursos };
});
