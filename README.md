# TouristAPI
Учебный проект в рамках стажеровки SkillFactory.
Для запуска проекта:
1) запустить docker-compose.yml
2) Отправить POST запрос по адресу http://127.0.0.1:1234/submitData с JSON в Body в соответствии с примером:

{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "test",
 
  "add_time": "2022-08-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"},
  "level": {"winter": "2D",
  "summer": "1А",
  "autumn": "1А",
  "spring": "2C"},
 
   "images": [{"data":"<картинка1>", "title":"Седловина"}, {"data":"<картинка>", "title":"Подъём"}]
}
