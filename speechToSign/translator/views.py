from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
import os

def home(request):
    return render(request, 'home.html')

def translate(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        recognizer = sr.Recognizer()
        recognized_text = ""
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                recognized_text = recognizer.recognize_google(audio)

            known_words = {
                'English': {'bad', 'begin', 'father', 'fine', 'good', 'i', 'like', 'mother', 'no', 'you', 'yes', 'know', 'understand'},
                'Spanish': {'bueno', 'padre', 'yo', 'intiendo', 'tu', 'no', 'si'}
            }

            recognized_words = set(recognized_text.lower().split())
            matched_words = recognized_words.intersection(known_words.get(language, set()))

            if matched_words:
                video_files = []
                for word in recognized_text.split():
                    video_file = f'{word}.mp4'
                    if os.path.exists(video_file):
                        video_files.append(video_file)
                return JsonResponse({'success': True, 'recognized_text': recognized_text, 'videos': video_files})
            else:
                return JsonResponse({'success': False, 'message': 'WORD NOT FOUND'})
        except sr.UnknownValueError:
            return JsonResponse({'success': False, 'message': "Sorry, I did not understand that."})
        except sr.RequestError:
            return JsonResponse({'success': False, 'message': "Sorry, there was an error with the request."})

    return JsonResponse({'success': False, 'message': "Invalid request method."})

def quit_app(request):
    return JsonResponse({'message': 'App terminated'})
