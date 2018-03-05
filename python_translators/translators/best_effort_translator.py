from python_translators.translators.composite_parallel_translator import CompositeParallelTranslator

from python_translators.factories.google_translator_factory import GoogleTranslatorFactory
from python_translators.factories.microsoft_translator_factory import MicrosoftTranslatorFactory
from python_translators.translators.glosbe_translator import GlosbeTranslator
from python_translators.translation_caches.memory_cache import MemoryCache


class BestEffortTranslator(CompositeParallelTranslator):
    def __init__(self, source_language: str, target_language: str):
        super(BestEffortTranslator, self).__init__(source_language=source_language, target_language=target_language)

        lang_config = dict(
            source_language=source_language,
            target_language=target_language
        )

        # Google Translator with context
        t = GoogleTranslatorFactory.build_contextless(**lang_config)
        t.quality = 80
        self.add_translator(t)

        # Google Translator without context
        t = GoogleTranslatorFactory.build_with_context(**lang_config)
        t.quality = 70
        self.add_translator(t)

        # Microsoft Translator without context
        t = MicrosoftTranslatorFactory.build_with_context(**lang_config)
        t.quality = 60
        self.add_translator(t)

        # Microsoft Translator without context
        t = MicrosoftTranslatorFactory.build_contextless(**lang_config)
        t.quality = 40
        self.add_translator(t)

        # Glosbe Translator without context
        #t = GlosbeTranslator(**lang_config)
        #t.quality = 30
        #self.add_translator(t)

        self.set_cache(MemoryCache(translator_type='best_effort_translator'))