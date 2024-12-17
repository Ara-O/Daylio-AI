import './assets/main.css'
import 'primeicons/primeicons.css'
import Aura from '@primevue/themes/aura'
import { definePreset } from '@primevue/themes'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ConfirmationService from 'primevue/confirmationservice'
import DialogService from 'primevue/dialogservice'

import ToastService from 'primevue/toastservice'

import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'

const app = createApp(App)

app.use(createPinia())
app.use(router)

const MyPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: '{lime.50}',
      100: '{lime.100}',
      200: '{lime.200}',
      300: '{lime.300}',
      400: '{lime.400}',
      500: '{lime.500}',
      600: '{lime.600}',
      700: '{lime.700}',
      800: '{lime.800}',
      900: '{lime.900}',
      950: '{lime.950}',
    },
    badgeWarnBackground: {
      DEFAULT: '{lime.100}', // Add your custom value
    },
  },
})

app.use(PrimeVue, {
  theme: {
    preset: MyPreset,
  },
})
app.use(ToastService)
app.use(ConfirmationService)
app.use(DialogService)

app.mount('#app')
