--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: vijay
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    age integer NOT NULL,
    gender character varying(20) NOT NULL
);


ALTER TABLE public.actors OWNER TO vijay;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: vijay
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO vijay;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vijay
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: vijay
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO vijay;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: vijay
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    release_date timestamp without time zone NOT NULL
);


ALTER TABLE public.movies OWNER TO vijay;

--
-- Name: movies_association; Type: TABLE; Schema: public; Owner: vijay
--

CREATE TABLE public.movies_association (
    actor_id integer NOT NULL,
    movie_id integer NOT NULL
);


ALTER TABLE public.movies_association OWNER TO vijay;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: vijay
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO vijay;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vijay
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: vijay
--

COPY public.actors (id, name, age, gender) FROM stdin;
1	barathi	68	male
2	vijay	30	male
4	barathi	68	male
5	vijay	68	male
6	vijay	20	male
7	vijay	20	male
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: vijay
--

COPY public.alembic_version (version_num) FROM stdin;
f2ed0eefd049
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: vijay
--

COPY public.movies (id, title, release_date) FROM stdin;
2	movie_title	2019-01-02 00:00:00
4	movie_title2	2019-01-02 00:00:00
5	movie_title4	2019-01-02 00:00:00
6	movie_title5	2019-01-02 00:00:00
\.


--
-- Data for Name: movies_association; Type: TABLE DATA; Schema: public; Owner: vijay
--

COPY public.movies_association (actor_id, movie_id) FROM stdin;
1	2
1	4
1	5
1	6
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vijay
--

SELECT pg_catalog.setval('public.actors_id_seq', 7, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vijay
--

SELECT pg_catalog.setval('public.movies_id_seq', 6, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: actors pk_actors; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT pk_actors PRIMARY KEY (id);


--
-- Name: movies pk_movies; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT pk_movies PRIMARY KEY (id);


--
-- Name: movies_association pk_movies_association; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.movies_association
    ADD CONSTRAINT pk_movies_association PRIMARY KEY (actor_id, movie_id);


--
-- Name: movies uq_movies_title; Type: CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT uq_movies_title UNIQUE (title);


--
-- Name: movies_association fk_movies_association_actor_id_actors; Type: FK CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.movies_association
    ADD CONSTRAINT fk_movies_association_actor_id_actors FOREIGN KEY (actor_id) REFERENCES public.actors(id);


--
-- Name: movies_association fk_movies_association_movie_id_movies; Type: FK CONSTRAINT; Schema: public; Owner: vijay
--

ALTER TABLE ONLY public.movies_association
    ADD CONSTRAINT fk_movies_association_movie_id_movies FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- PostgreSQL database dump complete
--

