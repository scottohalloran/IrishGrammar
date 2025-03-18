//
//  SampleData.swift
//  IrishVocabulary
//
//  Created by Scott O'Halloran on 12/8/24.
//

import Foundation
import SwiftData
@MainActor

class SampleData {
    static let shared = SampleData()
    let modelContainer: ModelContainer
    var context: ModelContext {
        modelContainer.mainContext
    }

    private init() {
        let schema = Schema([
            WordClass.self,
            WordListClass.self,
        ])
        
        let modelConfiguration = ModelConfiguration(schema: schema, isStoredInMemoryOnly: true)
        do {
            modelContainer = try ModelContainer(for: schema, configurations: [modelConfiguration])
            insertSampleData()
            try context.save()
        } catch {
            fatalError("Could not create ModelContainer: \(error)")
        }
    }

    private func insertSampleData() {
        for word in WordClass.sampleData {
            context.insert(word)
        }
        for wordList in WordListClass.sampleData {
             context.insert(wordList)
         }
    }
}
