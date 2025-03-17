<template>
  <v-footer height="auto" app color="primary" light>
    <v-container>
      <v-row justify="center" align="center">
        <v-col cols="12" md="6" class="text-center text-md-left">
          <p class="mb-1">
            <v-icon>mdi-email</v-icon>
            Entre em contato:
          </p>
          <p class="mb-1">
            <v-icon>mdi-email-outline</v-icon>
            Email:
            <a
              href="mailto:gustavojuniordos@hotmail.com"
              aria-label="Enviar e-mail para gustavojuniordos@hotmail.com"
              class="email-link"
            >
              gustavojuniordos@hotmail.com
            </a>
          </p>
          <p class="mb-1">
            <v-icon>mdi-phone</v-icon>
            Telefone: (43) 99619-5504
          </p>
        </v-col>
        <v-col cols="12" md="6" class="text-center text-md-right">
          <p class="mb-1">Siga-me nas redes sociais:</p>
          <v-btn icon href="https://www.linkedin.com/in/gustavo-junior-dos-santos/" target="_blank" aria-label="LinkedIn">
            <v-icon>mdi-linkedin</v-icon>
          </v-btn>
          <v-btn icon href="https://github.com/gustavodsantos" target="_blank" aria-label="GitHub">
            <v-icon>mdi-github</v-icon>
          </v-btn>
          <v-btn icon href="https://www.instagram.com/gustavo.jr.dos.santos/" target="_blank" aria-label="instagram">
            <v-icon>mdi-instagram</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" class="text-center">
          <p class="mb-0">&copy; {{ new Date().getFullYear() }} Gustavo Junior dos Santos. Todos os direitos reservados.</p>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  name: 'AppFooter',
};
</script>

<style scoped>
.email-link {
  color: inherit;
  text-decoration: none;
  font-weight: bold;
}

.email-link:hover {
  text-decoration: underline;
}
</style>
