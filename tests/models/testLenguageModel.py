from models.LanguageModel import LanguageModel
import pytest

def testGetLanguagesNotIsNone():
    languages = LanguageModel.getLanguages()
    assert languages is not None

def testGetLanguagesHaveItems():
    languages = LanguageModel.getLanguages()
    assert len(languages) > 0