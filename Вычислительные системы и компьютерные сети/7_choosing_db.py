"""
Выбор СУБД под задачу
Экспертами Яндекс.Облака подготовлена логическая схема для выбора СУБД в зависимости от критериев,
предъявляемых к ней.

Напишите программу, которая задаёт пользователю вопросы и рекомендует СУБД. Самая очевидная реализация -
множество условных конструкций if/else. Более удобный способ - описать граф и реализовать алгоритм его
обхода в зависимости от выбора пользователя. Оценка зависит от способа решения.
"""


class SubdRecommendationSystem:
    def __init__(self):
        self.graph = {
            'start': {
                'question': 'Данные структурированы?',
                'options': {
                    'Да': 'big_data',
                    'Нет': 'mean_stack',
                }
            },
            'big_data': {
                'question': 'Данных много?',
                'options': {
                    'Да': 'load_mixed',
                    'Нет': 'no_server',
                }
            },
            'load_mixed': {
                'question': 'Нагрузка смешанная?',
                'options': {
                    'Да': 'MongoDB',
                    'Нет': 'independent_stack',
                }
            },
            'independent_stack': {
                'question': 'Нужен технологически независимый стек?',
                'options': {
                    'Да': 'fast_development',
                    'Нет': 'microsoft',
                }
            },
            'fast_development': {
                'question': 'Нужна быстрая разработка?',
                'options': {
                    'Да': 'use_php',
                    'Нет': 'complex_data',
                }
            },
            'use_php': {
                'question': 'Используется PHP?',
                'options': {
                    'Да': 'MySQL',
                    'Нет': 'fast_development',
                }
            },
            'no_server': {
                'question': 'Используются бессерверные вычисления?',
                'options': {
                    'Да': 'YandexDatabase',
                    'Нет': 'MongoDB',
                }
            },
            'complex_data': {
                'question': 'Есть сложные операции с данными?',
                'options': {
                    'Да': 'admin_db',
                    'Нет': 'MySQL',
                }
            },
            'admin_db': {
                'question': 'Есть администратор баз данных?',
                'options': {
                    'Да': 'PostgreSQL',
                    'Нет': 'MySQL',
                }
            },
            'mean_stack': {
                'question': 'Используется стек MEAN?',
                'options': {
                    'Да': 'analytic_queries',
                    'Нет': 'modify_data',
                }
            },
            'analytic_queries': {
                'question': 'Основная цель - аналитические запросы?',
                'options': {
                    'Да': 'search',
                    'Нет': 'multidata',
                }
            },
            'search': {
                'question': 'Нужен ли полнотекстовый поиск?',
                'options': {
                    'Да': 'Elasticsearch',
                    'Нет': 'MongoDB',
                }
            },
            'multidata': {
                'question': 'Данных много?',
                'options': {
                    'Да': 'MongoDB',
                    'Нет': 'Redis',
                }
            },
            'modify_data': {
                'question': 'Нужно изменять данные?',
                'options': {
                    'Да': 'Elasticsearch',
                    'Нет': 'ClickHouse',
                }
            },
            'microsoft': {
                'question': 'Технологии Microsoft?',
                'options': {
                    'Да': 'MS SQL',
                    'Нет': 'YandexDatabase',
                }
            },
            'SQL Server': {
                'recommendation': 'Рекомендуется использовать SQL Server.',
            },
            'PostgreSQL': {
                'recommendation': 'Рекомендуется использовать PostgreSQL.',
            },
            'SQLite': {
                'recommendation': 'Рекомендуется использовать SQLite.',
            },
            'MongoDB': {
                'recommendation': 'Рекомендуется использовать MongoDB.',
            },
            'Cassandra': {
                'recommendation': 'Рекомендуется использовать Cassandra.',
            },
            'MySQL': {
                'recommendation': 'Рекомендуется использовать MySQL.',
            },
            'YandexDatabase': {
                'recommendation': 'Рекомендуется использовать YandexDatabase.',
            },
            'Elasticsearch': {
                'recommendation': 'Рекомендуется использовать Elasticsearch.',
            },
            'Redis': {
                'recommendation': 'Рекомендуется использовать Redis.',
            },
            'ClickHouse': {
                'recommendation': 'Рекомендуется использовать ClickHouse.',
            },
            'MS SQL': {
                'recommendation': 'Рекомендуется использовать MS SQL.',
            },
        }

    def recommend_subd(self):
        current_node = 'start'

        while True:
            node_data = self.graph[current_node]

            if 'recommendation' in node_data:
                print(node_data['recommendation'])
                break

            print(node_data['question'])
            for option, next_node in node_data['options'].items():
                print(f"- {option}")

            user_choice = input("Выберите вариант: ").strip()

            if user_choice in node_data['options']:
                current_node = node_data['options'][user_choice]
            else:
                print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    recommendation_system = SubdRecommendationSystem()
    recommendation_system.recommend_subd()
