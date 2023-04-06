//Самый главый массим обеъктов с вопросами весами
export const questions = [
  //     {
  //     text: 'Я ненавижу конкурировать ',
  //     answers: answers,
  //     onanswer: fn_answer({
  //         '0': {
  //             weight: 0.8,
  //             masks: ['**Н*', '**П*']
  //         },
  //         '1': {
  //             weight: 0.8,
  //             masks: ['**Б*', '**В*']
  //         },
  //         '2': {
  //             weight: 0.8,
  //             masks: ['**Б*', '**В*']
  //         }
  //     })
  // },
  {
    text: 'Время все расставит по местам ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.5,
        masks: []
      },
      '1': {
        weight: 1.5,
        masks: ['!*Б**']
      },
      '2': {
        weight: 1.5,
        masks: ['!*Б**']
      }
    })
  }, {
    text: 'Мне ничего не стоит вникнуть в чужой замысел и дополнить его ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.133333333333332,
        masks: ['Б***', 'В***', '*В**', '*Б**']
      },
      '1': {
        weight: 0.133333333333332,
        masks: []
      },
      '2': {
        weight: 0.133333333333332,
        masks: ['ПН**', 'НП**']
      }
    })
  }, {
    text: 'Я не могу придти в гости без приглашения ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.5,
        masks: []
      },
      '1': {
        weight: 1.5,
        masks: []
      },
      '2': {
        weight: 1.5,
        masks: ['!**Н*']
      }
    })
  }, {
    text: 'Я принимаю решения под влиянием момента ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.4,
        masks: ['Н***', '*Н**']
      },
      '1': {
        weight: 0.4,
        masks: ['**Н*', '***Н']
      },
      '2': {
        weight: 0.4,
        masks: ['**Н*', '***Н']
      }
    })
  }, {
    text: 'В прошлом слишком много неприятных воспоминаний, я предпочитаю не думать о них. ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: ['!***П']
      },
      '1': {
        weight: 0.5,
        masks: ['!**П*']
      },
      '2': {
        weight: 0.5,
        masks: ['!**П*']
      }
    })
  }, {
    text: 'Я хорошо понимаю кто я такой(ая)',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.2,
        masks: ['П***', '*П**']
      },
      '1': {
        weight: 1.2,
        masks: ['**П*', '***П']
      },
      '2': {
        weight: 1.2,
        masks: ['**П*', '***П']
      }
    })
  }, {
    text: 'Жизнь без приключений — ничто ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: ['!***П']
      },
      '1': {
        weight: 0.5,
        masks: []
      },
      '2': {
        weight: 0.5,
        masks: ['!П***']
      }
    })
  }, {
    text: 'У меня почти всегда есть план ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.7,
        masks: ['Б***']
      },
      '1': {
        weight: 0.7,
        masks: ['!Б***']
      },
      '2': {
        weight: 0.7,
        masks: ['!Б***']
      }
    })
  }, {
    text: 'Абсурд - это весело ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.7,
        masks: ['!**В*']
      },
      '1': {
        weight: 0.7,
        masks: ['**В*', '***В']
      },
      '2': {
        weight: 0.7,
        masks: []
      }
    })
  }, {
    text: 'Счастливые воспоминания легко приходят в голову ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: ['!**П*']
      },
      '1': {
        weight: 0.5,
        masks: []
      },
      '2': {
        weight: 0.5,
        masks: []
      }
    })
  }, {
    text: 'Удача дает больше чем упорная работа ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.75,
        masks: ['*Н**']
      },
      '1': {
        weight: 0.75,
        masks: []
      },
      '2': {
        weight: 0.75,
        masks: ['!*Н**']
      }
    })
  }, {
    text: 'Бездействие меня нервирует ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: ['Б***']
      },
      '1': {
        weight: 0.5,
        masks: []
      },
      '2': {
        weight: 0.5,
        masks: []
      }
    })
  },
  //  {
  //     text: 'Обожаю английский юмор ',
  //     answers: answers,
  //     onanswer: fn_answer({
  //         '0': {
  //             weight: 1.25,
  //             masks: ['В***', '*В**']
  //         },
  //         '1': {
  //             weight: 1.25,
  //             masks: []
  //         },
  //         '2': {
  //             weight: 1.25,
  //             masks: ['**В*', '***В']
  //         }
  //     })
  // },
  {
    text: 'Мои “скелеты в шкафу” вряд ли кому-нибудь интересны ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: []
      },
      '1': {
        weight: 0.5,
        masks: ['!***П']
      },
      '2': {
        weight: 0.5,
        masks: ['!***П']
      }
    })
  }, {
    text: 'Когда у меня есть цель, то все что к ней не относится перестает быть интересным ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.2,
        masks: ['БП**', 'Б*П*', 'Б**П', '*БП*', '*Б*П', '**БП']
      },
      '1': {
        weight: 1.2,
        masks: []
      },
      '2': {
        weight: 1.2,
        masks: ['ПБ**', 'П*Б*', 'П**Б', '*ПБ*', '*П*Б', '**ПБ']
      }
    })
  }, {
    text: 'Занимаясь чем-то я часто забываю про время ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.5,
        masks: []
      },
      '1': {
        weight: 1.5,
        masks: ['**Н*', '***Н']
      },
      '2': {
        weight: 1.5,
        masks: ['**Н*', '***Н']
      }
    })
  }, {
    text: 'Когда я не знаю что обо мне думают, меня это совершенно не волнует ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.666666666666667,
        masks: ['*П**', '***П']
      },
      '1': {
        weight: 0.666666666666667,
        masks: []
      },
      '2': {
        weight: 0.666666666666667,
        masks: ['П***', '**П*']
      }
    })
  }, {
    text: 'В идеале, хорошо было бы проживать каждый день как последний ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1,
        masks: ['Н***']
      },
      '1': {
        weight: 1,
        masks: []
      },
      '2': {
        weight: 1,
        masks: []
      }
    })
  }, {
    text: 'Мне трудно сориентироваться в незнакомом месте ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.8,
        masks: ['**Н*', '***Н']
      },
      '1': {
        weight: 0.8,
        masks: []
      },
      '2': {
        weight: 0.8,
        masks: ['Н***', '*Н**']
      }
    })
  }, {
    text: 'Все слишком изменчиво чтобы можно было планировать свое будущее ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.25,
        masks: ['**Б*', '***Б']
      },
      '1': {
        weight: 1.25,
        masks: []
      },
      '2': {
        weight: 1.25,
        masks: ['Б***', '*Б**']
      }
    })
  }, {
    text: 'В моем лице есть что-то детское ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: []
      },
      '1': {
        weight: 0.5,
        masks: ['!**П*']
      },
      '2': {
        weight: 0.5,
        masks: ['!**П*']
      }
    })
  }, {
    text: 'Мне нравится скорее принимать гостей, нежели ходить в гости ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.25,
        masks: ['Н***', '**Н*']
      },
      '1': {
        weight: 1.25,
        masks: []
      },
      '2': {
        weight: 1.25,
        masks: ['*Н**', '***Н']
      }
    })
  }, {
    text: 'Изучая что-то новое, я часто вижу скрытые закономерности, о которых нигде не говорится ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.8,
        masks: ['В***', '*В**']
      },
      '1': {
        weight: 0.8,
        masks: ['**В*', '***В']
      },
      '2': {
        weight: 0.8,
        masks: ['**В*', '***В']
      }
    })
  }, {
    text: 'Я легче чем многие переношу скуку ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1,
        masks: []
      },
      '1': {
        weight: 1,
        masks: []
      },
      '2': {
        weight: 1,
        masks: ['!***Н']
      }
    })
  }, {
    text: 'Коллекционирование - интереснейшее занятие ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: ['П***', '*П**']
      },
      '1': {
        weight: 0.5,
        masks: ['!П***']
      },
      '2': {
        weight: 0.5,
        masks: ['!П***']
      }
    })
  }, {
    text: 'Я далеко не всегда могу сказать зачем я делаю те или иные вещи ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.8,
        masks: ['**В*', '***В']
      },
      '1': {
        weight: 0.8,
        masks: []
      },
      '2': {
        weight: 0.8,
        masks: ['В***', '*В**']
      }
    })
  }, {
    text: 'Много раз я начинал(а) дела к котором, в итоге, оказывался(ась) совершенно неспособным ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.7,
        masks: ['***Б']
      },
      '1': {
        weight: 0.7,
        masks: []
      },
      '2': {
        weight: 0.7,
        masks: ['!***Б']
      }
    })
  }, {
    text: 'Придя в новый коллектив, я быстро становлюсь своим ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.5,
        masks: ['*Н**']
      },
      '1': {
        weight: 1.5,
        masks: ['*Н**', '***Н']
      },
      '2': {
        weight: 1.5,
        masks: []
      }
    })
  }, {
    text: 'Я воспринимаю мир не так ярко и живо как большинство моих знакомых ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: []
      },
      '1': {
        weight: 0.5,
        masks: ['!***Н']
      },
      '2': {
        weight: 0.5,
        masks: ['!***Н']
      }
    })
  }, {
    text: 'Мне легче говорить о вещах, которые не касаются меня лично ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.4,
        masks: ['ВП**', 'В*П*', 'В**П', '*ВП*', '*В*П', '**ВП']
      },
      '1': {
        weight: 0.4,
        masks: ['**В*', '***В']
      },
      '2': {
        weight: 0.4,
        masks: ['ПВ**', 'П*В*', 'П**В', '*ПВ*', '*П*В', '**ПВ']
      }
    })
  }, {
    text: 'Я принимаю каждый день, каков он есть, не пытаясь планировать его заранее ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.2,
        masks: ['НБ**', 'Н*Б*', 'Н**Б', '*НБ*', '*Н*Б', '**НБ']
      },
      '1': {
        weight: 1.2,
        masks: []
      },
      '2': {
        weight: 1.2,
        masks: ['БН**', 'Б*Н*', 'Б**Н', '*БН*', '*Б*Н', '**БН']
      }
    })
  }, {
    text: 'Импровизация - явно не мой жанр ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.4,
        masks: ['**Н*', '***Н']
      },
      '1': {
        weight: 0.4,
        masks: ['**Н*', '***Н']
      },
      '2': {
        weight: 0.4,
        masks: ['Н***', '*Н**']
      }
    })
  }, {
    text: 'Знания не бывают лишними ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.1,
        masks: ['П***']
      },
      '1': {
        weight: 0.1,
        masks: ['!П***']
      },
      '2': {
        weight: 0.1,
        masks: ['!П***']
      }
    })
  }, {
    text: 'Процесс перестает приносить мне удовольствие, если приходится думать о цели, последствиях и практических результатах ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.333333333333333,
        masks: ['**Б*', '***Б']
      },
      '1': {
        weight: 1.333333333333333,
        masks: []
      },
      '2': {
        weight: 1.333333333333333,
        masks: ['Б***', '*Б**']
      }
    })
  }, {
    text: 'Мои успехи редко видны со стороны ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1,
        masks: ['ПБ**', 'БП**']
      },
      '1': {
        weight: 1,
        masks: []
      },
      '2': {
        weight: 1,
        masks: []
      }
    })
  }, {
    text: 'Когда сразу несколько вещей требует внимания - я теряюсь ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.1,
        masks: ['***Н']
      },
      '1': {
        weight: 0.1,
        masks: ['!***Н']
      },
      '2': {
        weight: 0.1,
        masks: ['!***Н']
      }
    })
  }, {
    text: 'Мне приятно думать о прошлом ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.666666666666667,
        masks: []
      },
      '1': {
        weight: 0.666666666666667,
        masks: []
      },
      '2': {
        weight: 0.666666666666667,
        masks: ['П***', '**П*']
      }
    })
  }, {
    text: 'Я часто ощущаю себя лишним, ненужным ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.7,
        masks: ['**Н*']
      },
      '1': {
        weight: 0.7,
        masks: []
      },
      '2': {
        weight: 0.7,
        masks: ['!**Н*']
      }
    })
  }, {
    text: 'Судьба влияет на мою жизнь ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.1,
        masks: ['!***В']
      },
      '1': {
        weight: 0.1,
        masks: ['**В*', '***В']
      },
      '2': {
        weight: 0.1,
        masks: ['!**В*']
      }
    })
  }, {
    text: 'Как только дело закончено, я теряю к нему интерес ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.75,
        masks: ['БП**', 'Б*П*', 'Б**П', '*БП*', '*Б*П', '**БП']
      },
      '1': {
        weight: 0.75,
        masks: []
      },
      '2': {
        weight: 0.75,
        masks: ['ПБ**', 'П*Б*', 'П**Б', '*ПБ*', '*П*Б', '**ПБ']
      }
    })
  }, {
    text: 'Лучше потратить заработанные деньги на удовольствие сегодняшнего дня, чем отложить на черный день ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.4,
        masks: ['Н***', '*Н**']
      },
      '1': {
        weight: 0.4,
        masks: ['БН**', 'Б*Н*', 'Б**Н', '*БН*', '*Б*Н', '**БН']
      },
      '2': {
        weight: 0.4,
        masks: ['БН**', 'Б*Н*', 'Б**Н', '*БН*', '*Б*Н', '**БН']
      }
    })
  }, {
    text: 'Если не сидеть на месте, то обязательно подвернется какая-нибудь интересная возможность ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: []
      },
      '1': {
        weight: 0.5,
        masks: ['ПВ**', 'ВП**']
      },
      '2': {
        weight: 0.5,
        masks: ['ПВ**', 'ВП**']
      }
    })
  }, {
    text: 'Пусть я не стану специалистом, но понемножку буду разбираться во всём ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.1,
        masks: ['*П**']
      },
      '1': {
        weight: 0.1,
        masks: ['!*П**']
      },
      '2': {
        weight: 0.1,
        masks: ['!*П**']
      }
    })
  }, {
    text: 'Просьба рассказать о себе ставит меня в тупик ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.4,
        masks: ['**П*', '***П']
      },
      '1': {
        weight: 0.4,
        masks: []
      },
      '2': {
        weight: 0.4,
        masks: ['П***', '*П**']
      }
    })
  }, {
    text: 'Упреки в невежестве очень обидны ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.8,
        masks: ['В***', '**В*']
      },
      '1': {
        weight: 0.8,
        masks: []
      },
      '2': {
        weight: 0.8,
        masks: ['*В**', '***В']
      }
    })
  }, {
    text: 'Имея такую возможность, я бы несколько лет своей жизни посвятил путешествиям ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.5,
        masks: []
      },
      '1': {
        weight: 1.5,
        masks: ['!*Б**']
      },
      '2': {
        weight: 1.5,
        masks: ['!*Б**']
      }
    })
  }, {
    text: 'Я умею смеяться над собой ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1.5,
        masks: []
      },
      '1': {
        weight: 1.5,
        masks: ['!*В**']
      },
      '2': {
        weight: 1.5,
        masks: ['!*В**']
      }
    })
  }, {
    text: 'Когда мне нечем заняться, я чувствую себя опустошенным(ной)',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.3,
        masks: ['**Н*']
      },
      '1': {
        weight: 0.3,
        masks: ['!**Н*']
      },
      '2': {
        weight: 0.3,
        masks: ['!**Н*']
      }
    })
  }, {
    text: 'Настоящий мир скрыт от посторонних глаз ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: ['!***В']
      },
      '1': {
        weight: 0.5,
        masks: ['!В***']
      },
      '2': {
        weight: 0.5,
        masks: ['!В***']
      }
    })
  }, {
    text: 'Знание будущего - проклятье а не дар ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 1,
        masks: ['**Б*']
      },
      '1': {
        weight: 1,
        masks: []
      },
      '2': {
        weight: 1,
        masks: []
      }
    })
  }, {
    text: 'Я быстро забываю о неудаче и двигаюсь дальше ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.5,
        masks: ['*П**', '***П']
      },
      '1': {
        weight: 0.5,
        masks: []
      },
      '2': {
        weight: 0.5,
        masks: ['П***', '**П*']
      }
    })
  }, {
    text: 'Мой дом - моя крепость ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.75,
        masks: ['!***П']
      },
      '1': {
        weight: 0.75,
        masks: []
      },
      '2': {
        weight: 0.75,
        masks: ['!П***']
      }
    })
  }, {
    text: 'Часто перед тем как что-то начать делать я испытываю нервозность или даже страх ',
    answers: answers,
    onanswer: fn_answer({
      '0': {
        weight: 0.833333333333333,
        masks: ['!*Б**']
      },
      '1': {
        weight: 0.833333333333333,
        masks: []
      },
      '2': {
        weight: 0.833333333333333,
        masks: ['!**Б*']
      }
    })
  },
];