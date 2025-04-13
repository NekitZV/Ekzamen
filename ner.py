from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsNERTagger,
    NewsMorphTagger,
    MorphVocab,
    Doc
)

# Инициализация моделей
segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
ner_tagger = NewsNERTagger(emb)
morph_vocab = MorphVocab()

def mu_ner(text, entity_type=None):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.tag_ner(ner_tagger)

    if entity_type is None:
        # Просто размеченный текст
        for span in doc.spans:
            span.normalize(morph_vocab)
            text = text.replace(span.text, f"[{span.normal} <{span.type}>]")
        return text
    else:
        # Вернем список нормализованных сущностей нужного типа
        results = []
        for span in doc.spans:
            if span.type == entity_type:
                span.normalize(morph_vocab)
                results.append(span.normal)
        return results
