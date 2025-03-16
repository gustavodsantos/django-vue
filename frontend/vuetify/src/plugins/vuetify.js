/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import * as components from 'vuetify/components'; // Importa todos os componentes do Vuetify
import * as directives from 'vuetify/directives'; // Importa todas as diretivas do Vuetify

// Composables
import { createVuetify } from 'vuetify'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  components, // Registra todos os componentes
  directives, // Registra todas as diretivas
  theme: {
    defaultTheme: 'dark',
  },
})
