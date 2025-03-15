<template>

  <v-app-bar app color="primary">
    <v-app-bar-title>Menu</v-app-bar-title>

    <v-spacer></v-spacer>

    <v-menu offset-y>
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props">
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </template>

      <v-list>
        <v-list-item @click="login">
          <v-list-item-icon>
            <v-icon>mdi-login</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Login</v-list-item-title>
        </v-list-item>
        <v-list-item @click="register">
          <v-list-item-icon>
            <v-icon>mdi-account-plus</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Registrar</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>

</template>

<script setup>
  import { useRouter } from 'vue-router';

  const router = useRouter();

  const login = () => {
    router.push('/login');  // Navega para a rota de login
  };

  const register = () => {
    router.push('/register');  // Navega para a rota de registro
  };
</script>
