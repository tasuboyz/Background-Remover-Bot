class Language:
    def __init__(self):
        self.visual_qr_reply = ["Generate Visual QR 🌉", "Genera QR Visivo 🌉", "विजुअल क्यूआर बनाएं 🌉", "Generar QR Visual 🌉", "Générer un QR Visuel 🌉", "Generiere visuellen QR 🌉", "Создать визуальный QR 🌉", "Створити візуальний QR 🌉"]
        self.normal_qr_reply = ["Generate Normal QRcode 🌱", "Genera QRcode Normale 🌱", "सामान्य QRकोड बनाएं 🌱", "Generar Código QR Normal 🌱", "Générer un QRcode Normal 🌱", "Generiere normalen QRcode 🌱", "Создать обычный QR-код 🌱", "Створити звичайний QR-код 🌱"]
        self.custom_background_reply = ["Custom Background 🔥", "Sfondo Personalizzato 🔥", "कस्टम पृष्ठभूमि 🔥", "Fondo Personalizado 🔥", "Benutzerdefinierter Hintergrund 🔥", "Индивидуальный фон 🔥", "Індивідуальний фон 🔥"]
        self.custom_foreground_reply = ["Custom Foreground", "Personalizza Primo Piano", "कस्टम पहला प्लान", "Primer plano personalizado", "Arrière-plan Personnalisé", "Benutzerdefinierter Vordergrund", "Индивидуальный передний план", "Індивідуальний передній план"]
        self.previus_color_reply = ["previous color 🎨", "colore precedente 🎨", "पिछला रंग 🎨", "color anterior 🎨", "couleur précédente 🎨", "vorherige Farbe 🎨", "предыдущий цвет 🎨", "попередній колір 🎨"]
        self.version = ["Version"]
        self.advanced = ["Advanced"]
        
    def start_lang(self, first_name, language_code):
        channel_link = '<a href="https://t.me/tasu_Channel">👇</a>'    
        eng = (f"Hello {first_name}! 👋 Welcome to my bot!\n"
                       "📸 Send me an image, and I'll remove the background for you.\n"
                       "\n"
                       "🎨 You can customize the result by choosing a color or sending an image for the background.\n"
                       "\n"
                       f"{channel_link} Follow the channel for updates!")    
        if language_code == 'it':
            message = (f"Ciao {first_name}! 👋 Benvenuto nel mio bot!\n"
                       "📸 Inviami un'immagine e rimuoverò lo sfondo per te.\n"
                       "\n"
                       "🎨 Puoi personalizzare il risultato scegliendo un colore o inviando un'immagine per lo sfondo.\n"
                       "\n"
                       f"{channel_link} Segui il canale per gli aggiornamenti!")
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = (f"नमस्ते {first_name} 👋, मेरे बॉट में आपका स्वागत है!\n"
                       "📸 मुझे एक छवि भेजें, और मैं आपके लिए पृष्ठभूमि हटा दूंगा।\n"
                       "\n"
                       "🎨 आप एक रंग चयन करके या पृष्ठभूमि के लिए एक छवि भेजकर परिणाम को व्यक्तिगतकृत कर सकते हैं।\n"
                       "\n"
                       f"{channel_link} अपडेट के लिए चैनल का अनुसरण करें!")
        elif language_code == 'es':
            message = (f"Hola {first_name} 👋, ¡Bienvenido a mi bot!\n"
                       "📸 Envíame una imagen y eliminaré el fondo para ti.\n"
                       "\n"
                       "🎨 Puedes personalizar el resultado eligiendo un color o enviando una imagen para el fondo.\n"
                       "\n"
                       f"{channel_link} ¡Sigue el canal para recibir actualizaciones!")
        elif language_code == 'fr':
            message = (f"Bonjour {first_name} 👋, Bienvenue dans mon bot !\n"
                       "📸 Envoyez-moi une image, et je supprimerai l'arrière-plan pour vous.\n"
                       "\n"
                       "🎨 Vous pouvez personnaliser le résultat en choisissant une couleur ou en envoyant une image pour l'arrière-plan.\n"
                       "\n"
                       f"{channel_link} Suivez le canal pour les mises à jour !")
        elif language_code == 'de':
            message = (f"Hallo {first_name} 👋, Willkommen in meinem Bot!\n"
                       "📸 Schick mir ein Bild, und ich entferne den Hintergrund für dich.\n"
                       "\n"
                       "🎨 Du kannst das Ergebnis anpassen, indem du eine Farbe wählst oder ein Bild für den Hintergrund sendest.\n"
                       "\n"
                       f"{channel_link} Folge dem Kanal für Updates!")
        elif language_code == 'ru':
            message = (f"Привет {first_name} 👋, Добро пожаловать в мой бот!\n"
                       "📸 Отправьте мне изображение, и я удалю фон для вас.\n"
                       "\n"
                       "🎨 Вы можете настроить результат, выбрав цвет или отправив изображение для фона.\n"
                       "\n"
                       f"{channel_link} Подпишитесь на канал, чтобы получать обновления!")
        elif language_code == 'uk':
            message = (f"Привіт {first_name} 👋, Ласкаво просимо до мого бота!\n"
                       "📸 Надішліть мені зображення, і я видалю фон для вас.\n"
                       "\n"
                       "🎨 Ви можете налаштувати результат, вибравши колір або відправивши зображення для фону.\n"
                       "\n"
                       f"{channel_link} Слідкуйте за каналом, щоб отримувати оновлення!")
        else:
            message = eng
        return message

    def back(self, language_code):
        eng = "Back 🔙"
        if language_code == 'it':
            message = "Indietro 🔙"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "पीछे 🔙"
        elif language_code == 'es':
            message = "Volver 🔙"
        elif language_code == 'fr':
            message = "Retour 🔙"
        elif language_code == 'de':
            message = "Zurück 🔙"
        elif language_code == 'ru':
            message = "Назад 🔙"
        elif language_code == 'uk':
            message = "Назад 🔙"
        else:
            message = eng
        return message
    
    def cancel(self, language_code):
        eng = "Cancel ❌"
        if language_code == 'it':
            message = "Annulla ❌"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "रद्द करें ❌"
        elif language_code == 'es':
            message = "Cancelar ❌"
        elif language_code == 'fr':
            message = "Annuler ❌"
        elif language_code == 'de':
            message = "Abbrechen ❌"
        elif language_code == 'ru':
            message = "Отмена ❌"
        elif language_code == 'uk':
            message = "Відмінити ❌"
        else:
            message = eng
        return message

    def waiting(self, language_code):
        eng = "Waiting..."
        if language_code == 'it':
            message = "In attesa..."
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "प्रतीक्षा कर रहा हूँ..."
        elif language_code == 'es':
            message = "Esperando..."
        elif language_code == 'fr':
            message = "En attente..."
        elif language_code == 'de':
            message = "Warten..."
        elif language_code == 'ru':
            message = "Ожидание..."
        elif language_code == 'uk':
            message = "Очікування..."
        else:
            message = eng
        return message

    def error(self, language_code):
        eng = "Ops... an error has occurred 😔 contact owner or try again!"
        if language_code == 'it':
            message = "Ops... si è verificato un errore 😔 contatta il proprietario o riprova!"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "ओह... कुछ गड़बड़ हो गई है 😔 मालिक से संपर्क करें या पुनः प्रयास करें!"
        elif language_code == 'es':
            message = "Ops... ha ocurrido un error 😔 contacta al propietario o inténtalo de nuevo."
        elif language_code == 'fr':
            message = "Ops... une erreur s'est produite 😔 contactez le propriétaire ou réessayez !"
        elif language_code == 'de':
            message = "Oops... ein Fehler ist aufgetreten 😔 kontaktiere den Besitzer oder versuche es erneut!"
        elif language_code == 'ru':
            message = "Упс... произошла ошибка 😔 свяжитесь с владельцем или попробуйте снова!"
        elif language_code == 'uk':
            message = "Ой... сталася помилка 😔 зверніться до власника або спробуйте ще раз!"
        else:
            message = eng
        return message
    
    def file_not_valid(self, language_code):
        eng = "The image file is not valid 🚫"
        if language_code == 'it':
            message = "Il file dell'immagine non è valido 🚫"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "चित्र फ़ाइल मान्य नहीं है 🚫"
        elif language_code == 'es':
            message = "El archivo de imagen no es válido 🚫"
        elif language_code == 'fr':
            message = "Le fichier image n'est pas valide 🚫"
        elif language_code == 'de':
            message = "Die Bilddatei ist nicht gültig 🚫"
        elif language_code == 'ru':
            message = "Файл изображения недопустим 🚫"
        elif language_code == 'uk':
            message = "Файл зображення недійсний 🚫"
        else:
            message = eng
        return message

    def code_not_found(self, language_code):
        eng = "No code found or unable to decode it 🚫"
        if language_code == 'it':
            message = "Nessun codice trovato o impossibile decodificarlo 🚫"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "कोई कोड नहीं मिला या इसे डिकोड करने में असमर्थ 🚫"
        elif language_code == 'es':
            message = "No se encontró ningún código o no se puede decodificar 🚫"
        elif language_code == 'fr':
            message = "Aucun code trouvé ou incapable de le décoder 🚫"
        elif language_code == 'de':
            message = "Kein Code gefunden oder nicht entschlüsselbar 🚫"
        elif language_code == 'ru':
            message = "Код не найден или не удается его декодировать 🚫"
        elif language_code == 'uk':
            message = "Код не знайдено або не вдається його розкодувати 🚫"
        else:
            message = eng
        return message

    def choose_color(self, language_code):
        eng = "Choose color 🎨"
        if language_code == 'it':
            message = "Scegli il colore 🎨"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "रंग चुनें 🎨"
        elif language_code == 'es':
            message = "Elige un color 🎨"
        elif language_code == 'fr':
            message = "Choisissez la couleur 🎨"
        elif language_code == 'de':
            message = "Farbe wählen 🎨"
        elif language_code == 'ru':
            message = "Выберите цвет 🎨"
        elif language_code == 'uk':
            message = "Виберіть колір 🎨"
        else:
            message = eng
        return message

    def open_link(self, language_code):
        eng = "Open Link"
        if language_code == 'it':
            message = "Apri il link"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "लिंक खोलें"
        elif language_code == 'es':
            message = "Abrir enlace"
        elif language_code == 'fr':
            message = "Ouvrir le lien"
        elif language_code == 'de':
            message = "Link öffnen"
        elif language_code == 'ru':
            message = "Открыть ссылку"
        elif language_code == 'uk':
            message = "Відкрити посилання"
        else:
            message = eng
        return message

    def confirm(self, language_code, qr):
        caption_status = '✅' if qr else '⚠️'
        eng = f"Confirm {caption_status}"
        if language_code == 'it':
            message = f"Conferma {caption_status}"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"पुष्टि {caption_status}"
        elif language_code == 'es':
            message = f"Confirmar {caption_status}"
        elif language_code == 'fr':
            message = f"Confirmer {caption_status}"
        elif language_code == 'de':
            message = f"Bestätigen {caption_status}"
        elif language_code == 'ru':
            message = f"Подтвердить {caption_status}"
        elif language_code == 'uk':
            message = f"Підтвердити {caption_status}"
        else:
            message = eng
        return message

    def confirmed(self, language_code, qr):        
        eng = 'Readable ✅' if qr else 'Your qr is unreadable (internally)⚠️'
        if language_code == 'it':
            message = 'Leggibile ✅' if qr else 'Il tuo codice QR non è leggibile (internamente)⚠️'
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = 'अधिपठनीय ✅' if qr else 'आपका क्यूआर अधिपठनीय नहीं है (आंतरिक रूप से)⚠️'
        elif language_code == 'es':
            message = 'Legible ✅' if qr else 'Su código QR no es legible (internamente)⚠️'
        elif language_code == 'fr':
            message = 'Lisible ✅' if qr else 'Votre QR code n\'est pas lisible (en interne)⚠️'
        elif language_code == 'de':
            message = 'Lesbar ✅' if qr else 'Ihr QR-Code ist nicht lesbar (intern)⚠️'
        elif language_code == 'ru':
            message = 'Читаемо ✅' if qr else 'Ваш QR-код нечитаем (внутренне)⚠️'
        elif language_code == 'uk':
            message = 'Читабельний ✅' if qr else 'Ваш QR-код нечитабельний (внутрішньо)⚠️'
        else:
            message = eng
        return message
    
    def rembg_mode(self, language_code):
        eng = "Choose color 🎨 or send me another image 🌉:"
        if language_code == 'it':
            message = "Scegli il colore 🎨 o inviami un'altra immagine 🌉:"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "रंग चुनें 🎨 या मुझे एक और छवि भेजें 🌉:"
        elif language_code == 'es':
            message = "Elige un color 🎨 o envíame otra imagen 🌉:"
        elif language_code == 'fr':
            message = "Choisissez une couleur 🎨 ou envoyez-moi une autre image 🌉:"
        elif language_code == 'de':
            message = "Wählen Sie eine Farbe 🎨 oder senden Sie mir ein anderes Bild 🌉:"
        elif language_code == 'ru':
            message = "Выберите цвет 🎨 или отправьте мне другое изображение 🌉:"
        elif language_code == 'uk':
            message = "Виберіть колір 🎨 або надішліть мені інше зображення 🌉:"
        else:
            message = eng
        return message
    
    def operation_deleted(self, language_code):
        eng = "operation deleted 🗑"
        if language_code == 'it':
            message = "operazione eliminata 🗑"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "कार्रवाई हटा दी गई 🗑"
        elif language_code == 'es':
            message = "operación eliminada 🗑"
        elif language_code == 'fr':
            message = "opération supprimée 🗑"
        elif language_code == 'de':
            message = "Operation gelöscht 🗑"
        elif language_code == 'ru':
            message = "операция удалена 🗑"
        elif language_code == 'uk':
            message = "операцію видалено 🗑"
        else:
            message = eng
        return message
    
    def back(self, language_code):
        eng = "Back 🔙"
        if language_code == 'it':
            message = "Indietro 🔙"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = "पिछला रंग 🎨"
        elif language_code == 'es':
            message = "Volver 🔙"
        elif language_code == 'fr':
            message = "Retour 🔙"
        elif language_code == 'de':
            message = "Zurück 🔙"
        elif language_code == 'ru':
            message = "Назад 🔙"
        elif language_code == 'uk':
            message = "Назад 🔙"
        else:
            message = eng
        return message
    
    def not_member_channel(self, language_code):
        channel_link = '<a href="https://t.me/tasu_Channel">👇</a>'
        eng = f"Join the channel to take advantage of the function! {channel_link}"
        if language_code == 'it':
            message = f"Entra nel canale per usufruire della funzione! {channel_link}"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"कार्रवाई का लाभ उठाने के लिए चैनल में शामिल हों! {channel_link}"
        elif language_code == 'es':
            message = f"¡Entra al canal para utilizar esta función! {channel_link}"
        elif language_code == 'fr':
            message = f"Inscrivez-vous sur le canal pour bénéficier de la fonctionnalité! {channel_link}"
        elif language_code == 'de':
            message = f"Tritt dem Kanal bei, um die Funktion zu nutzen! {channel_link}"
        elif language_code == 'ru':
            message = f"Вступите в канал, чтобы воспользоваться функцией! {channel_link}"
        elif language_code == 'uk':
            message = f"Приєднуйтесь до каналу, щоб скористатися функцією! {channel_link}"
        else:
            message = eng
        return message
    
    def loading(self, language_code):
        eng = f"Please wait for the loading ❗️"
        if language_code == 'it':
            message = f"Perfavore attendi il caricamento ❗️"
        elif language_code == 'en':
            message = eng
        elif language_code == 'hi':
            message = f"कृपया लोड होने का इंतजार करें ❗️"
        elif language_code == 'es':
            message = f"Por favor espera mientras carga ❗️"
        elif language_code == 'fr':
            message = f"Veuillez patienter pendant le chargement ❗️"
        elif language_code == 'de':
            message = f"Bitte warten Sie, während geladen wird ❗️"
        elif language_code == 'ru':
            message = f"Пожалуйста, подождите, пока загрузка не завершится ❗️"
        elif language_code == 'uk':
            message = f"Будь ласка, зачекайте, поки завантажується ❗️"
        else:
            message = eng
        return message




