-- Footdle: 매일 유럽 5대리그 축구선수 한 명 맞추기
-- 선수/팀 데이터: API-Football 또는 Transfermarkt 에서 가져와서 players, teams 에 저장
-- 입력 후보: players 테이블에서 이름으로 검색

CREATE TABLE users (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    username   VARCHAR(30) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 소속팀 / 데뷔팀 둘 다 여기서 참조
CREATE TABLE teams (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    name      VARCHAR(50) NOT NULL UNIQUE,
    league    ENUM('EPL', 'LALIGA', 'SERIE_A', 'BUNDESLIGA', 'LIGUE_1') NULL,  -- 데뷔팀은 5대리그 밖일 수 있어서 NULL 허용
    rank_2526 INT NULL                                                        -- 2025-26 리그 최종 순위
);

CREATE TABLE players (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(50) NOT NULL,
    birth_year    INT NOT NULL,
    nationality   VARCHAR(30) NOT NULL,
    position      ENUM('GK', 'DF', 'MF', 'FW') NOT NULL,
    team_id       INT NOT NULL,          -- 현 소속팀 (순위는 teams 에서)
    debut_team_id INT NOT NULL,          -- 프로 데뷔팀 (ex. 각포 -> PSV)
    league_titles INT NOT NULL DEFAULT 0, -- 선수 본인 리그 우승 횟수
    ucl_titles    INT NOT NULL DEFAULT 0, -- 선수 본인 챔스 우승 횟수
    height_cm     INT NOT NULL,
    FOREIGN KEY (team_id)       REFERENCES teams(id),
    FOREIGN KEY (debut_team_id) REFERENCES teams(id)
);

-- 날짜마다 정답 한 명
CREATE TABLE daily_puzzles (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    date      DATE NOT NULL UNIQUE,
    player_id INT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(id)
);

-- 유저가 어느 날 몇 번째로 누굴 찍었고, 8개 항목 결과가 뭐였는지
CREATE TABLE guesses (
    id                INT AUTO_INCREMENT PRIMARY KEY,
    user_id           INT NOT NULL,
    puzzle_id         INT NOT NULL,
    player_id         INT NOT NULL,
    attempt_no        INT NOT NULL,
    birth_year_hint   ENUM('UP', 'DOWN', 'EQUAL') NOT NULL,
    nationality_match BOOLEAN NOT NULL,
    position_match    BOOLEAN NOT NULL,
    rank_hint         ENUM('UP', 'DOWN', 'EQUAL') NOT NULL,
    league_titles_hint ENUM('UP', 'DOWN', 'EQUAL') NOT NULL,
    ucl_titles_hint   ENUM('UP', 'DOWN', 'EQUAL') NOT NULL,
    debut_team_match  BOOLEAN NOT NULL,
    height_hint       ENUM('UP', 'DOWN', 'EQUAL') NOT NULL,
    created_at        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)   REFERENCES users(id),
    FOREIGN KEY (puzzle_id) REFERENCES daily_puzzles(id),
    FOREIGN KEY (player_id) REFERENCES players(id),
    UNIQUE (user_id, puzzle_id, attempt_no)
);
