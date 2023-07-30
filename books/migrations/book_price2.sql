-- liquibase formatted sql

-- changeset kuzanagi:1690748156689-1
CREATE TABLE "books" ("id" UUID NOT NULL, "name" VARCHAR(100) NOT NULL, "author" VARCHAR(100) NOT NULL, "ean" VARCHAR(15), "price" numeric(5, 2) NOT NULL, CONSTRAINT "books_pkey" PRIMARY KEY ("id"));

