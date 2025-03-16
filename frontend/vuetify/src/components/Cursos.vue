<script setup>
  import { useCursosStore } from '@/stores/cursos';
  import { onMounted, ref } from 'vue';

  const store = useCursosStore();
  const { cursos } = store;
  const loading = ref(true);
  const error = ref(null);

onMounted(async () => {
  console.log('Componente montado. Buscando cursos...');  // Verifique no console
  try {
    await store.fetchCursos();
  } catch (error) {
    error.value = 'Erro ao carregar cursos. Tente novamente mais tarde.';
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row v-if="cursos.length > 0">
          <v-col v-for="curso in cursos" :key="curso.url" class="border rounded-lg" cols="12" md="4">
            <v-card>
              <v-card-title>{{ curso.titulo }}</v-card-title>
              <v-card-text>{{ curso.descricao }}</v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row v-else>
          <v-col cols="12">
            <v-alert type="info">Carregando cursos...</v-alert>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped lang="sass">

</style>
