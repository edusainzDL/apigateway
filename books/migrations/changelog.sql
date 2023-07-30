-- liquibase formatted sql

-- changeset kuzanagi:1690748267066-1
CREATE TABLE "books" ("id" UUID NOT NULL, "name" VARCHAR(100) NOT NULL, "author" VARCHAR(100) NOT NULL, "ean" VARCHAR(15), "price" numeric(12, 2) NOT NULL, CONSTRAINT "books_pkey" PRIMARY KEY ("id"));

