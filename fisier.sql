--
-- PostgreSQL database dump
--

\restrict s9QiMIpVmNfaDvxebrDixNYOKB4SEbIW9fbu4yBo2dBtHeez3ZMBs2u4AUKSElI

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_autor; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (1, 'Eliade', 'Mircea', '1907-03-13');
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (2, 'Preda', 'Marin', '1922-08-05');
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (3, 'Dostoyevski', 'Fiodor M.', '1821-11-11');
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (4, 'Rebreanu', 'Liviu', '1885-11-27');
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (7, 'Homer', NULL, NULL);
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (8, 'Zaharia', 'Maria', NULL);
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (9, 'Zaharia', 'Dan', NULL);
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (10, 'Peligrad', 'Sorin', NULL);
INSERT INTO django.aplicatie_exemplu_autor (id, nume, prenume, data_nastere) VALUES (11, 'Brown', 'Dan', NULL);


--
-- Name: aplicatie_exemplu_autor_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_autor_id_seq', 10, true);


--
-- PostgreSQL database dump complete
--

\unrestrict s9QiMIpVmNfaDvxebrDixNYOKB4SEbIW9fbu4yBo2dBtHeez3ZMBs2u4AUKSElI

--
-- PostgreSQL database dump
--

\restrict szQRd8PPFa0f6SBnM3Xwg0ffEUMnjPGEhb8V0leYVmesM385oc4ZweIGu4BLpbz

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_editura; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_editura (id, nume_editura) VALUES (1, 'RAO');
INSERT INTO django.aplicatie_exemplu_editura (id, nume_editura) VALUES (3, 'Humanitas');
INSERT INTO django.aplicatie_exemplu_editura (id, nume_editura) VALUES (4, 'Dacia');
INSERT INTO django.aplicatie_exemplu_editura (id, nume_editura) VALUES (5, 'Academia Romana');
INSERT INTO django.aplicatie_exemplu_editura (id, nume_editura) VALUES (6, 'Historia');


--
-- Name: aplicatie_exemplu_editura_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_editura_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

\unrestrict szQRd8PPFa0f6SBnM3Xwg0ffEUMnjPGEhb8V0leYVmesM385oc4ZweIGu4BLpbz

--
-- PostgreSQL database dump
--

\restrict jaJG5dCvrCJD5ISL1nco6ZYi3sEiPiV3KL7Y4jMX0EgwX5Eu6xqP2SeMahLHFu2

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_categorie; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (3, 'Polițist', 'Gen literar axat pe rezolvarea unei crime sau a unui mister. Se caracterizează prin suspans intens, anchete detaliate și adesea include elemente psihologice sau de acțiune rapidă.', 'politist', '#AAAAAA');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (5, 'Teatru & Dramaturgie', 'Colecții de piese de teatru, scenarii și lucrări care explorează arta dramatică. Ideal pentru studenți, actori și pasionații de spectacole.', 'teatru-dramaturgie', '#AAAAAA');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (6, 'Știință & Tehnologie', 'Lucrări non-ficționale care explorează domenii științifice (fizică, biologie, astronomie), inovații tehnologice și concepte teoretice complexe.', 'stiinta-tehnologie', '#AAAAAA');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (8, 'Dezvoltare Personală', 'Cărți menite să inspire și să ghideze cititorul în îmbunătățirea calității vieții, a mentalității, a relațiilor sau a carierei.', 'dezvoltare-personala', '#AAAAAA');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (2, 'Fictiune', 'Cărți bazate pe întâmplări și personaje imaginate, care nu sunt ancorate strict în realitate. Include opere literare, romane și povestiri.', 'fictiune', '#F4BA33');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (4, 'Educație', 'Materiale didactice, manuale școlare, ghiduri de studiu și cărți care facilitează învățarea academică sau dezvoltarea de noi competențe practice.', 'educatie', '#AA33BB');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (9, 'Istorie', 'Lucrări care explorează evenimente, epoci, civilizații și personalități din trecut, bazate pe cercetări factuale și documente istorice.', 'istorie', '#FFF432');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (7, 'Fantasy & SF', 'Genuri care includ lumi imaginare, magie, ființe mitologice (Fantasy) sau explorări futuriste, călătorii spațiale și concepte științifice avansate (Science Fiction).', 'fantasy-sf', '#BB1000');
INSERT INTO django.aplicatie_exemplu_categorie (id, nume, descriere, slug, culoare_hex) VALUES (1, 'Biografie', 'Cartile biografice au ca obiectiv principal familiarizarea cititorului cu persoana (persoanele) prezentata si intreaga prezentarea se invarte in jurul acesteia.', 'biografie', '#AAAA33');


--
-- Name: aplicatie_exemplu_categorie_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_categorie_id_seq', 9, true);


--
-- PostgreSQL database dump complete
--

\unrestrict jaJG5dCvrCJD5ISL1nco6ZYi3sEiPiV3KL7Y4jMX0EgwX5Eu6xqP2SeMahLHFu2

--
-- PostgreSQL database dump
--

\restrict gvs8CAL0CyXbuFpgcDx9Cn1f1RwnmYCzPTCvb35J6960htnKT87ijky1T7jO6T6

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_carte; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (2, 'Crima si Pedeapsa', 1866, 10.00, 'documente/Crima_si_pedeapsa.jpeg', 1, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (12, 'Culegere Clasa a V-a', 20, 10.00, 'documente/clasa_a_V_a.webp', 5, 4);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (1, 'Delirul', 1991, 10.00, 'documente/delirul.png', 3, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (8, 'Domnisoara Christina', 1936, 10.00, 'documente/domnisoara_christina.jpeg', 3, 7);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (3, 'Idiotul', 1868, 10.00, 'documente/idiotul.jpg', 1, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (4, 'Iliada', NULL, 10.00, 'documente/Iliada.jpg', 3, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (6, 'Ion', 1920, 10.00, 'documente/Ion.jpeg', 3, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (0, 'Maytrei', 1933, 10.00, 'documente/maitreyi.jpeg', 3, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (9, 'Noaptea de Sanziene', 1971, 10.00, 'documente/noaptea_de_sanziene.jpeg', 3, 7);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (7, 'Nunta in cer', 1939, 10.00, 'documente/nunta_in_cer.jpeg', 3, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (5, 'Odiseea', NULL, 10.00, 'documente/odissea.jpg', 3, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (10, 'Romanul adolescentului miop', 1928, 10.00, 'documente/romanul_adolescentului_miop.jpeg', 3, 1);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (2123123213, 'Simbolul Pierdut', NULL, 58.90, '', 1, 2);
INSERT INTO django.aplicatie_exemplu_carte ("ISBN", titlu, an_publicatie, pret, imagine, id_editura_id, categorie_id) VALUES (1234561234, 'Secretul Secretelor', NULL, 31.90, '', 1, NULL);


--
-- PostgreSQL database dump complete
--

\unrestrict gvs8CAL0CyXbuFpgcDx9Cn1f1RwnmYCzPTCvb35J6960htnKT87ijky1T7jO6T6

--
-- PostgreSQL database dump
--

\restrict MoqXKCfsK6inmFNqJQrHByV8pE4iijZXMclKx9D5jmuzyAX6DaTeAjZaxLfgdgx

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_copiecarte; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (1, false, NULL, 'Romana', 2, NULL);
INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (2, false, NULL, 'Romana', 2, 1);
INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (3, false, NULL, 'Romana', 0, 1);
INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (4, false, NULL, 'Romana', 0, NULL);
INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (5, false, NULL, 'Romana', 5, NULL);
INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (6, false, '', 'Romana', 4, NULL);
INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (7, true, '', 'Romana', 8, 2);
INSERT INTO django.aplicatie_exemplu_copiecarte (id_copie, semnat_de_autor, observatii, limba, isbn_id, id_oferta_id) VALUES (8, true, '', 'Romana', 0, 1);


--
-- Name: aplicatie_exemplu_copiecarte_id_copie_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_copiecarte_id_copie_seq', 8, true);


--
-- PostgreSQL database dump complete
--

\unrestrict MoqXKCfsK6inmFNqJQrHByV8pE4iijZXMclKx9D5jmuzyAX6DaTeAjZaxLfgdgx

--
-- PostgreSQL database dump
--

\restrict mehQusraP5aqzwkQabWamAnldT4rDxpDc4s3lWUQ9dipPRIeYR3RjRYnQNGOKCo

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_oferta; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_oferta (id_oferta, titlu, procent_reducere) VALUES (1, 'nimic', 15);
INSERT INTO django.aplicatie_exemplu_oferta (id_oferta, titlu, procent_reducere) VALUES (2, 'Black Friday', 15);


--
-- Name: aplicatie_exemplu_oferta_id_oferta_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_oferta_id_oferta_seq', 2, true);


--
-- PostgreSQL database dump complete
--

\unrestrict mehQusraP5aqzwkQabWamAnldT4rDxpDc4s3lWUQ9dipPRIeYR3RjRYnQNGOKCo

--
-- PostgreSQL database dump
--

\restrict 34arEvTpumP1df3533uoM47EM2zsDPWSR29HIgdVc5pG6o1qZZf8pehK9XcqsXV

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_antichitate; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_antichitate (id_antichitate, tip_obiect, id_oferta_id) VALUES (1, 'vaza', NULL);
INSERT INTO django.aplicatie_exemplu_antichitate (id_antichitate, tip_obiect, id_oferta_id) VALUES (2, 'vaza', 1);
INSERT INTO django.aplicatie_exemplu_antichitate (id_antichitate, tip_obiect, id_oferta_id) VALUES (3, 'tablou', NULL);
INSERT INTO django.aplicatie_exemplu_antichitate (id_antichitate, tip_obiect, id_oferta_id) VALUES (4, 'tablou', NULL);
INSERT INTO django.aplicatie_exemplu_antichitate (id_antichitate, tip_obiect, id_oferta_id) VALUES (5, 'obiect_muzeal', 2);
INSERT INTO django.aplicatie_exemplu_antichitate (id_antichitate, tip_obiect, id_oferta_id) VALUES (6, 'vaza', NULL);


--
-- Name: aplicatie_exemplu_antichitate_id_antichitate_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_antichitate_id_antichitate_seq', 6, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 34arEvTpumP1df3533uoM47EM2zsDPWSR29HIgdVc5pG6o1qZZf8pehK9XcqsXV

--
-- PostgreSQL database dump
--

\restrict 2IJjvrvL5eSOpGeKU2oUTtKgDWISF0hVN44XfaGzxBbBKCebiczguWLcZKVivxG

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_abonament; Type: TABLE DATA; Schema: django; Owner: matei
--



--
-- Name: aplicatie_exemplu_abonament_id_abonament_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_abonament_id_abonament_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict 2IJjvrvL5eSOpGeKU2oUTtKgDWISF0hVN44XfaGzxBbBKCebiczguWLcZKVivxG

--
-- PostgreSQL database dump
--

\restrict wLyM1VB6OxksIRqxznIEjbCuMdB7sb2QhaoXrvazr9TTUwoBm7Irjrduz3c8j7m

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_carte_autor; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (15, 2, 3);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (16, 12, 8);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (17, 12, 9);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (18, 12, 10);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (19, 1, 2);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (20, 8, 1);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (21, 3, 3);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (22, 4, 7);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (23, 6, 4);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (24, 0, 1);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (25, 9, 1);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (26, 7, 1);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (27, 5, 7);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (28, 10, 1);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (29, 2123123213, 11);
INSERT INTO django.aplicatie_exemplu_carte_autor (id, carte_id, autor_id) VALUES (30, 1234561234, 11);


--
-- Name: aplicatie_exemplu_carte_autor_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_carte_autor_id_seq', 14, true);


--
-- PostgreSQL database dump complete
--

\unrestrict wLyM1VB6OxksIRqxznIEjbCuMdB7sb2QhaoXrvazr9TTUwoBm7Irjrduz3c8j7m

--
-- PostgreSQL database dump
--

\restrict Av1xgF6EVCoDzSIU2WmqE38zgcj8POrXHFZXfFfj7iTWYX2VBvHurALd4yz4ea1

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_comanda; Type: TABLE DATA; Schema: django; Owner: matei
--



--
-- Name: aplicatie_exemplu_comanda_id_comanda_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_comanda_id_comanda_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict Av1xgF6EVCoDzSIU2WmqE38zgcj8POrXHFZXfFfj7iTWYX2VBvHurALd4yz4ea1

--
-- PostgreSQL database dump
--

\restrict 5drnuldGq2R4IMysBv45FkaahhoyZvzXJf1oeCLrvk1tapYBTptYoFv1nqhkSlX

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_utilizator; Type: TABLE DATA; Schema: django; Owner: matei
--



--
-- Name: aplicatie_exemplu_utilizator_id_user_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_utilizator_id_user_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict 5drnuldGq2R4IMysBv45FkaahhoyZvzXJf1oeCLrvk1tapYBTptYoFv1nqhkSlX

--
-- PostgreSQL database dump
--

\restrict n2p3mmYZTc3DzvzD7TtFLuXelaCnQIkOFqrlc9OWQgwUAHf9V40Vnyp5VGKBLIl

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.1 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_exemplu_voucher; Type: TABLE DATA; Schema: django; Owner: matei
--



--
-- Name: aplicatie_exemplu_voucher_id_voucher_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie_exemplu_voucher_id_voucher_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict n2p3mmYZTc3DzvzD7TtFLuXelaCnQIkOFqrlc9OWQgwUAHf9V40Vnyp5VGKBLIl

