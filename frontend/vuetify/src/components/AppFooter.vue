<template>
  <v-footer height="auto" app color="primary" light>
    <v-container>
      <v-row justify="center" align="center">
        <v-col cols="12" md="6" class="text-center text-md-left">
          <p class="mb-1">Entre em contato:</p>
          <p class="mb-1">
            Email:
            <a
              href="mailto:gustavojuniordos@hotmail.com"
              aria-label="Enviar e-mail para gustavojuniordos@hotmail.com"
              class="email-link"
            >
              gustavojuniordos@hotmail.com
            </a>
          </p>
          <p class="mb-1">Telefone: (43) 99619-5504</p>
        </v-col>

        <v-col cols="12" md="6" class="text-center text-md-right">
          <p class="mb-1">Redes Sociais:</p>
          <v-btn
            variant="text"
            color="white"
            href="https://www.linkedin.com/in/gustavo-junior-dos-santos/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <v-icon left>mdi-linkedin</v-icon>
            LinkedIn
          </v-btn>
          <v-btn
            variant="text"
            color="white"
            href="https://github.com/gustavodsantos"
            target="_blank"
            rel="noopener noreferrer"
          >
            <v-icon left>mdi-github</v-icon>
            GitHub
          </v-btn>
        </v-col>
      </v-row>

      <v-divider class="my-1"></v-divider>

      <v-row justify="center">
        <v-col cols="12" class="text-center">
          <span class="text-caption">
            &copy; {{ new Date().getFullYear() }} Gustavo Junior dos Santos. Todos os direitos reservados.
          </span>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script setup>
// Nenhuma lógica adicional é necessária para este componente.
</script>

<style scoped lang="sass">
  .v-footer
    padding: 5px 0
    background-color: rgba(33, 33, 33, 0.9) /* Fundo mais discreto */

  .v-btn
    margin: 0 8px

  .email-link
    color: #0D47A1
    text-decoration: none
    transition: color 0.3s ease

    &:hover
      color: #E3F2FD /* Cor mais clara ao passar o mouse */
      text-decoration: underline

  .text-caption
    font-size: 0.8rem /* Tamanho menor para o texto de direitos autorais */
</style>
