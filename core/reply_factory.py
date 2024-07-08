
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
    return True, ""


def get_next_question(current_question_id):
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''

    from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST, CORRECT_ANSWERS


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
    if current_question_id is None:
        return False, "No current question ID found."

    # Validate the answer if needed (for example, check if the answer is in a specific format)
    # For simplicity, let's assume all answers are valid

    # Store the answer in the session
    if "answers" not in session:
        session["answers"] = {}
    session["answers"][current_question_id] = answer
    return True, ""


def get_next_question(current_question_id):
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''
    if current_question_id is None:
        # Start from the first question if no current question ID
        next_question_id = 0
    else:
        next_question_id = current_question_id + 1

    if next_question_id < len(PYTHON_QUESTION_LIST):
        next_question = PYTHON_QUESTION_LIST[next_question_id]
        return next_question, next_question_id
    else:
        # No more questions left
        return None, None


def generate_final_response(session):
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''
    answers = session.get("answers", {})
    score = 0

    for question_id, user_answer in answers.items():
        correct_answer = CORRECT_ANSWERS.get(question_id)
        if user_answer == correct_answer:
            score += 1

    total_questions = len(PYTHON_QUESTION_LIST)
    result_message = f"You have completed the quiz! Your score is {score} out of {total_questions}."
    return result_message


def generate_final_response(session):
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''

    answers = session.get("answers", {})
    score = 0

    for question_id, user_answer in answers.items():
        correct_answer = CORRECT_ANSWERS.get(question_id)
        if user_answer == correct_answer:
            score += 1

    total_questions = len(PYTHON_QUESTION_LIST)
    result_message = f"You have completed the quiz! Your score is {score} out of {total_questions}."
    return result_message
